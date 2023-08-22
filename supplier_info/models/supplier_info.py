# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SupplierInfo(models.Model):
    """
    To add supplier info
    """
    _name = "supplier.info"
    _description = "Supplier Info"

    purchase_order_id = fields.Many2one("purchase.order")
    product_id = fields.Many2one("product.product")
    vendor_id = fields.Many2one("res.partner")
    product_qty = fields.Integer("Quantity")
    price = fields.Integer("Price")

    # Action Methods

    def action_create_po(self):
        """
        To create purchase order
        """
        self.env["purchase.order"].create({
            "partner_id": self.vendor_id.id,
            "order_line": [(fields.Command.create({
                "product_id": self.product_id.id,
                "product_qty": self.product_qty,
                "price_unit": self.price,
            }))],
        })
