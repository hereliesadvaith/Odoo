# -*- coding: utf-8 -*-
from odoo import fields, models


class ComparePrice(models.TransientModel):
    """
    Model for wizard
    """
    _name = "compare.price"

    supplier_ids = fields.Many2many("supplier.info")
