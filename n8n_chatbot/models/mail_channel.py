# -*- coding: utf-8 -*-
from odoo import api, models
from markupsafe import Markup
import logging


_logger = logging.getLogger(__name__)


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
                self.sudo().message_post(
                    body=Markup("hey there"),
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
