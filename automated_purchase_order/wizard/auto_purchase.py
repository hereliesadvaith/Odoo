# -*- coding: utf-8 -*-

from odoo import fields, models


class AutoPurchase(models.TransientModel):
    """
    Model for wizard
    """
    _name = "auto.purchase"
    _description = "Auto Purchase"

    product_id = fields.Many2one("product.product", string="Product",
                                 readonly=True)
    quantity = fields.Integer(string="Quantity", default=1)
    price = fields.Integer(string="Price", required=True)
    vendor = fields.Many2one("res.partner", string="Vendor", required=True)

    # seller_ids = fields.One2many('product.supplierinfo', 'product_tmpl_id')

    # Action Methods

    def action_confirm(self):
        """
        Creates a purchase order
        """
        purchase_order = self.env["purchase.order"].search([
            ('state', '=', 'draft'),
            ('partner_id', '=', self.vendor.id),
        ], order="id desc", limit=1)
        if purchase_order:
            purchase_order.update({
                "order_line": [(fields.Command.create({
                    "product_id": self.product_id.id,
                    "product_qty": self.quantity,
                    "price_unit": self.price
                }))],
            })
            purchase_order.button_confirm()
        else:
            new_purchase_order = self.env["purchase.order"].create({
                "partner_id": self.vendor.id
            })
            new_purchase_order.update({
                "order_line": [(fields.Command.create({
                    "product_id": self.product_id.id,
                    "product_qty": self.quantity,
                    "price_unit": self.price
                }))],
            })
            new_purchase_order.button_confirm()
