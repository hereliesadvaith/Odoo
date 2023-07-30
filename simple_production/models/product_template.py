# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductsTemplate(models.Model):
    """
    To add fields to product template model.
    """

    _inherit = "product.template"

    manufacture_ok = fields.Boolean(
        string="Can be Manufactured", help="Check product can be manufactured")
