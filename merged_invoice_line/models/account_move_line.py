# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountMoveLine(models.Model):
    """
    To inherit create invoice button
    """
    _inherit = 'account.move.line'

    sale_order_names = fields.Char("Sale Orders")
