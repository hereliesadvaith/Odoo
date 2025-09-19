# -*- coding: utf-8 -*-
from odoo import api, models
from markupsafe import Markup


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
            self.sudo().message_post(
                body=Markup("Hello, I’m your AI bot!"),
                message_type="comment",
                subtype_xmlid="mail.mt_comment",
                author_id=agents[0].id,
            )
        return res
