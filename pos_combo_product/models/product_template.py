# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductsTemplate(models.Model):
    """
    To add fields to product template model.
    """
    _inherit = "product.template"

    is_combo = fields.Boolean(
        string="Is Combo", help="Check if the product have combo products")
    combo_product_ids = fields.One2many("combo.product",
                                    "product_tmpl_id",
                                    help="Combo Products")
    
