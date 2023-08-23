# -*- coding: utf-8 -*-
from odoo import fields, models


class ComparePrice(models.TransientModel):
    """
    Model for wizard
    """
    _name = "compare.price"
    _description = "Compare Price"

    supplier_ids = fields.Many2many("supplier.info",
                                    help="Supplier info in wizard")
