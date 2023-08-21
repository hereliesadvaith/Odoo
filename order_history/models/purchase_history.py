# -*- coding: utf-8 -*-
from odoo import fields, models


class PurchaseHistory(models.Model):
    """
    To save order history
    """
    _name = "purchase.history"
    _description = "Purchase Order"

    order_history_id = fields.Many2one("order.history",
                                       help="Order History id")
    purchase_id = fields.Many2one("purchase.order",
                                  help="Purchase order")
    vendor_id = fields.Many2one("res.partner",
                                help="Vendor", related="purchase_id.partner_id")
