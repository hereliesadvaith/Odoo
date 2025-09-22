# -*- coding: utf-8 -*-
from odoo import fields, models


class ChatbotAccess(models.Model):
    """
    To store functions available for specific bot.
    """
    _name = "chatbot.access"
    _description = "Chatbot Access"

    chatbot_script_id = fields.Many2one("chatbot.script",
                                        help="Chatbot Id")
    ir_model_id = fields.Many2one("ir.model", "Model",
                                  help="Available model")
    ir_model_fields_ids = fields.Many2many(
        'ir.model.fields',
        string='Fields',
        domain='[("model_id", "=", ir_model_id)]',
        help="Available fields"
    )
