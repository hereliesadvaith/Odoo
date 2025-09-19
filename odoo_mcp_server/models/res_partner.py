# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    """
    Inherit model res.partner.
    """
    _inherit = "res.partner"

    is_agent = fields.Boolean("AI Agent", help="Is AI Agent ?")
