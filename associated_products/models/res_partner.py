# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    """
    To add fields in invoice page.
    """

    _inherit = "res.partner"

    associated_product_ids = fields.Many2many("product.product")
