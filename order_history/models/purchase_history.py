# -*- coding: utf-8 -*-
from odoo import fields, models


class PurchaseHistory(models.Model):
    """
    To save order history
    """
    _name = "purchase.history"
    _description = "Purchase Order"

    order_history_id = fields.Many2one("order.history")
    purchase_id = fields.Many2one("purchase.order")
    vendor_id = fields.Many2one("res.partner")
