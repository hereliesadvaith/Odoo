# -*- coding: utf-8 -*-
import json
from odoo import api, fields, models
from odoo.tools import config
from markupsafe import Markup
import google.generativeai as genai
import logging


_logger = logging.getLogger(__name__)

genai.configure(api_key=config["google_api_key"])
model = genai.GenerativeModel("gemini-2.5-flash")

tools = [
    {
        "function_declarations": [
            {
                "name": "rpc_for_llm",
                "description": "Call an Odoo model method with given arguments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model": {
                            "type": "string",
                            "description": "Odoo model name (e.g. res.partner, sale.order)"
                        },
                        "method": {
                            "type": "string",
                            "description": "Method to call (e.g. search_read, create)"
                        },
                        "args": {
                            "type": "array",
                            "description": "Positional arguments list",
                            "items": {}  # no constraints
                        },
                        "kwargs": {
                            "type": "object",
                            "description": "Keyword arguments dictionary",
                            "properties": {}  # no constraints
                        }
                    },
                    "required": ["model", "method"]
                }
            }
        ]
    }
]


class MailChannel(models.Model):
    """
    Inherit discuss.channel.
    """
    _inherit = "discuss.channel"

    ai_chat_history = fields.Json("AI Chat History", help="Chat history")

    @api.model
    def message_post(self, **kwargs):
        """
        Super message_post to add AI reply.
        """
        res = super().message_post(**kwargs)
        self.env.cr.commit()
        agents = self.channel_partner_ids.filtered(
            lambda x: any(bot.is_agent for bot in x.chatbot_script_ids)
        )
        if agents and not any(
                bot.is_agent for bot in res.author_id.chatbot_script_ids
        ):
            try:
                chat = model.start_chat(history=self._deserialize_history(
                    self.ai_chat_history or []) or [])
                response = chat.send_message(
                    str(kwargs.get("body")),
                    tools=tools,
                )
                if response.candidates[0].content.parts[0].function_call:
                    function_call = response.candidates[0].content.parts[
                        0].function_call
                    data = self.rpc_for_llm(**function_call.args)
                    response = chat.send_message(
                        json.dumps(data)
                    )
                    self.sudo().message_post(
                        body=Markup(response.text),
                        message_type="comment",
                        subtype_xmlid="mail.mt_comment",
                        author_id=agents[0].id,
                    )
                    self.sudo().write({
                        "ai_chat_history": self._serialize_history(chat.history)
                    })
                elif response.text:
                    self.sudo().message_post(
                        body=Markup(response.text),
                        message_type="comment",
                        subtype_xmlid="mail.mt_comment",
                        author_id=agents[0].id,
                    )
                    self.sudo().write({
                        "ai_chat_history": self._serialize_history(chat.history)
                    })
            except Exception as e:
                _logger.warning(f"AI Agent Error: {e}")
                self.sudo().message_post(
                    body=Markup("Something went wrong."),
                    message_type="comment",
                    subtype_xmlid="mail.mt_comment",
                    author_id=agents[0].id,
                )
        return res

    @staticmethod
    def _serialize_history(history):
        """
        Convert history (Content objects) into JSON-serializable.
        """
        serialized = []
        for item in history:
            serialized.append({
                "role": item.role,
                "parts": [p.text for p in item.parts if hasattr(p, "text")],
            })
        return serialized

    @staticmethod
    def _deserialize_history(history_json):
        """
        Convert stored JSON back into compatible history.
        """
        return [
            {"role": h["role"],
             "parts": [{"text": p} for p in h.get("parts", [])]}
            for h in history_json
        ]

    def rpc_for_llm(self, **payload):
        odoo_model = payload.get("model")
        method = payload.get("method")
        args = payload.get("args") or []
        kwargs = {k: v for k, v in payload.get(
            "kwargs").items()} if payload.get("kwargs") else {}
        if hasattr(self.env[odoo_model], method):
            return getattr(self.env[odoo_model], method)(*args, **kwargs)
        else:
            raise ValueError(f"Method {method} not found on model {model}")
