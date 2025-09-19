# -*- coding: utf-8 -*-
from odoo import api, models
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

    @api.model
    def message_post(self, **kwargs):
        """
        Super message_post to add AI reply.
        """
        res = super().message_post(**kwargs)
        agents = self.channel_partner_ids.filtered(
            lambda x: x.is_agent
        )
        if agents and not res.author_id.is_agent:
            try:
                response = model.generate_content(str(kwargs.get("body")))
                self.sudo().message_post(
                    body=Markup(response.text),
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
