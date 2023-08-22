# -*- coding: utf-8 -*-
from odoo import models, fields


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
    is_best_price = fields.Boolean("Best Price", default=False)

    # Action Methods

    def action_create_po(self):
        """
        To create purchase order
        """
        for order in self.purchase_order_id.order_line:
            if order.product_id == self.product_id:
                order.unlink()
        self.purchase_order_id._create_supplier_info()
        self.env["purchase.order"].create({
            "partner_id": self.vendor_id.id,
            "order_line": [(fields.Command.create({
                "product_id": self.product_id.id,
                "product_qty": self.product_qty,
                "price_unit": self.price,
            }))],
        })
