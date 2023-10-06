# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):
    """
    To add fields in contact creation page.
    """
    _inherit = "res.partner"

    enable_purchase_limit = fields.Boolean("Purchase Limit",
                                           help="Balance due")
    purchase_limit_value = fields.Float("Limit", help="Add limit")
    total_session_amount = fields.Float(help="session_amount")
