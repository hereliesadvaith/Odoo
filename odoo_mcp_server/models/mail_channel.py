# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.tools import config
from markupsafe import Markup
import google.generativeai as genai
import logging


_logger = logging.getLogger(__name__)

genai.configure(api_key=config["google_api_key"])
model = genai.GenerativeModel("gemini-2.5-flash")


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
                response = chat.send_message(str(kwargs.get("body")))
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

    def _serialize_history(self, history):
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

    def _deserialize_history(self, history_json):
        """
        Convert stored JSON back into compatible history.
        """
        return [
            {"role": h["role"],
             "parts": [{"text": p} for p in h.get("parts", [])]}
            for h in history_json
        ]
