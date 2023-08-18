# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    """
    To add fields to product template model.
    """
    _inherit = "product.template"

    manufacture_ok = fields.Boolean(
        string="Can be Manufactured", help="Check product can be manufactured")
    component_ids = fields.One2many("required.component",
                                    "product_tmpl_id",
                                    help="components")
