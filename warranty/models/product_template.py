# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductsTemplate(models.Model):
    """
    To add fields to product template model.
    """

    _inherit = "product.template"

    has_warranty = fields.Boolean(string="Has Warranty")
    warranty_type = fields.Selection(
        string="Warranty Type",
        selection=[
            ("service_warranty", "Service Warranty"),
            ("replacement_warranty", "Replacement Warranty"),
        ],
        required=True,
    )
    warranty_period = fields.Integer(string="Warranty Period(Days)", required=True)
