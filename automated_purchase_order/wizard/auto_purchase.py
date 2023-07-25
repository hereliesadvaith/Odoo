# -*- coding: utf-8 -*-

from odoo import fields, models


class AutoPurchase(models.TransientModel):
    """
    Model for wizard
    """
    _name = "auto.purchase"
    _description = "Auto Purchase"

    quantity = fields.Integer(string="Qty", default=1)
    price = fields.Integer(string="Price")
