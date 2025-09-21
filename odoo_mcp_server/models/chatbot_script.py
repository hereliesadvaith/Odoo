# -*- coding: utf-8 -*-
from odoo import fields, models


class ChatbotScript(models.Model):
    """
    Inherit model chatbot.script.
    """
    _inherit = "chatbot.script"

    is_agent = fields.Boolean("AI Agent", help="Is AI Agent ?")

    def action_generate_agent_user(self):
        """
        Generate user for chatbot.
        """
        if not self.operator_partner_id.user_ids:
            self.sudo().write({
                'is_agent': True
            })
            self.env['res.users'].sudo().create([{
                "name": self.operator_partner_id.name,
                "partner_id": self.operator_partner_id.id,
                "login": self.operator_partner_id.name.lower()
            }])
