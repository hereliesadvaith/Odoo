# -*- coding: utf-8 -*-
from odoo import models


class InventoryDashboard(models.AbstractModel):
    """
    To get values for inventory dashboard.
    """
    _name = "inventory.dashboard"
    _description = "Inventory Dashboard"

    # Action Methods

    def get_incoming_stock(self, domain):
        """
        To get incoming stocks
        """
        products = self.env["product.product"].sudo().search(domain).filtered(
            lambda r: r.incoming_qty > 0)
        return {
            "labels": [i.name for i in products],
            "data": [i.incoming_qty for i in products]
        }

    def get_outgoing_stock(self, domain):
        """
        To get outgoing stocks
        """
        products = self.env["product.product"].sudo().search(domain).filtered(
            lambda r: r.outgoing_qty > 0)
        return {
            "labels": [i.name for i in products],
            "data": [i.outgoing_qty for i in products]
        }

    def get_internal_transfer(self, domain):
        """
        To get internal transfers
        """
        stock_moves = self.env["stock.move"].search([
            ("picking_type_id", "=", self.env.ref(
                "stock.picking_type_internal"
            ).id),
            ("state", "not in", ["done", "cancel"]),
        ])
        internal_transfers, products = [], []
        for product in stock_moves.mapped("product_id"):
            quantity = 0
            for rec in stock_moves.filtered(lambda r: r.product_id == product):
                quantity += rec.product_uom_qty
            products.append(product.name)
            internal_transfers.append(quantity)
        return {
            "labels": products,
            "data": internal_transfers,
        }

    def get_average_expense(self, domain):
        """
        To get average expense of products.
        """
        products = self.env["product.product"].sudo().search(domain).filtered(
            lambda r: r.qty_available > 0)
        return {
            "labels": [i.name for i in products],
            "data": [i.avg_cost for i in products]
        }

    def get_inventory_valuation(self, domain):
        """
        To get datas for inventory valuation
        """
        products = self.env["product.product"].sudo().search(domain).filtered(
            lambda r: r.qty_available > 0)
        return {
            "labels": [i.name for i in products],
            "data": [(i.avg_cost * i.qty_available) for i in products]
        }

    def get_stock_location(self, domain):
        """
        To get warehouse location based stock
        """
        products = self.env["product.product"].sudo().search(domain).filtered(
            lambda r: r.qty_available > 0)
        stock_quant_ids = self.env["stock.quant"].sudo().search([]).filtered(
            lambda r: r.location_id.usage == "internal"
        )
        print(stock_quant_ids)
        return [[i.location_id.name, i.product_id.name, i.inventory_quantity_auto_apply] for i in stock_quant_ids]
