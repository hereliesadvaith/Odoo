# -*- coding: utf-8 -*-
from odoo import models


class InventoryDashboard(models.AbstractModel):
    """
    To get values for inventory dashboard.
    """

    _name = "inventory.dashboard"
    _description = "Inventory Dashboard"

    def get_stock_incoming(self, domain):
        """
        To get incoming stocks
        """
        print(domain)
        products = self.env["product.product"].sudo().search(domain).filtered(
            lambda r: r.incoming_qty > 0)
        print(products)
        return {
            "products": [i.name for i in products],
            "incoming_qty": [i.incoming_qty for i in products]
        }

    def get_stock_outgoing(self, domain):
        """
        To get outgoing stocks
        """
        print(domain)
        products = self.env["product.product"].sudo().search(domain).filtered(
            lambda r: r.outgoing_qty > 0)
        print(products)
        return {
            "products": [i.name for i in products],
            "outgoing_qty": [i.outgoing_qty for i in products]
        }

    def get_internal_transfer(self, domain):
        """
        To get internal transfers
        """
        print(domain)
        stock_moves = self.env["stock.move"].search([
            ("picking_type_id", "=", self.env.ref(
                "stock.picking_type_internal"
            ).id),
            ("state", "not in", ["done", "cancel"]),
        ])
        internal_transfers, products = [], []
        for product in stock_moves.mapped("product_id"):
            quantity = 0
            products.append(product.name)
            for rec in stock_moves.filtered(lambda r: r.product_id == product):
                quantity += rec.product_uom_qty
            internal_transfers.append(quantity)
        return {
            "products": products,
            "internal_transfers": internal_transfers,
        }
