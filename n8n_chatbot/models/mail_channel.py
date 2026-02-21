# -*- coding: utf-8 -*-
from markupsafe import Markup
from odoo import api, models
import requests
import logging


_logger = logging.getLogger(__name__)
n8n_endpoint = "http://localhost:5678/webhook/ai_agent"


class MailChannel(models.Model):
    """
    Inherit discuss.channel.
    """
    _inherit = "discuss.channel"

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
                response = requests.post(
                    n8n_endpoint,
                    json={
                        "chatInput": kwargs.get('body'),
                        "sessionId": self.uuid
                    }
                )
                data = response.json()
                self.sudo().message_post(
                    body=Markup(data[0].get('output')),
                    message_type="comment",
                    subtype_xmlid="mail.mt_comment",
                    author_id=agents[0].id,
                )
            except Exception as e:
                _logger.warning(f"AI Agent Error: {e}")
                self.sudo().message_post(
                    body=Markup("Something went wrong."),
                    message_type="comment",
                    subtype_xmlid="mail.mt_comment",
                    author_id=agents[0].id,
                )
        return res
