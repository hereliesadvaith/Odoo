# -*- coding: utf-8 -*-
from odoo import fields, models


class RequiredComponent(models.Model):
    """
    To add list of components and quantity required
    """
    _name = "required.component"
    _description = "Required Component"

    product_tmpl_id = fields.Many2one("product.template")
    simple_production_id = fields.Many2one("simple.production")
    product_id = fields.Many2one("product.product", help="Product")
    quantity = fields.Integer(string="Quantity", help="Quantity")
    source_location_id = fields.Many2one("stock.location",
                                         string="Source Location",
                                         help="Source location")
