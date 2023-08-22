# -*- coding: utf-8 -*-
from odoo import fields, models


class ComparePrice(models.TransientModel):
    """
    Model for wizard
    """
    _name = "compare.price"

    purchase_order_id = fields.Integer("id")
    supplier_ids = fields.Many2many("supplier.info")
