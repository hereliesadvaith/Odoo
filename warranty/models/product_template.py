# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductsTemplate(models.Model):
    """
    To add fields to product template model.
    """

    _inherit = "product.template"

    has_warranty = fields.Boolean(string="Has Warranty")
    warranty_type_id = fields.Many2one("warranty.type", string="Warranty Type")
    warranty_period = fields.Integer(string="Warranty Period(Days)")
