# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    """
    To add fields in contact creation page.
    """
    _inherit = "res.partner"

    associated_product_ids = fields.Many2many(
        "product.product", help="Associated products")
