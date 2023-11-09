# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    """
    To inherit sales order page.
    """
    _inherit = "sale.order"

    associated_products = fields.Boolean(
        string="Associated Products", help="Check to add associated products")