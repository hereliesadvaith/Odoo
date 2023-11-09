# -*- coding: utf-8 -*-
from odoo import api, fields, models


class QualityMeasure(models.Model):
    """
    Model for Quality Measure.
    """
    _name = "quality.measure"
    _description = "Quality Measure"

    name = fields.Char("Name", help="Name", required=True)
    product_id = fields.Many2one("product.product", string="Product",
                                 required=True, help="Product")
    test_type = fields.Selection(selection=[
        ("quantity", "Quantitative"),
        ("quality", "Qualitative")
    ], string="Test Type", help="Test type", default="quantity")
    active = fields.Boolean("Active", default=True)
    trigger_ids = fields.Many2many("stock.picking.type", string="Trigger On",
                                   help="Trigger on")
