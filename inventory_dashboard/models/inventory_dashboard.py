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
        domain.append(["picking_type_id", "=", self.env.ref(
            "stock.picking_type_in"
        ).id])
        if self.env.user not in self.env.ref("stock.group_stock_manager").users:
            domain.append(["create_uid", "=", self.env.context["uid"]])
        stock_moves = self.env["stock.move"].search(domain)
        purchase_orders, products = [], []
        for product in stock_moves.mapped("product_id").filtered(
                lambda r: r.detailed_type == "product"
        ):
            quantity = 0
            for rec in stock_moves.filtered(lambda r: r.product_id == product):
                quantity += rec.product_uom_qty
            products.append(product.name)
            purchase_orders.append(quantity)
        return {
            "labels": products,
            "data": purchase_orders,
        }

    def get_outgoing_stock(self, domain):
        """
        To get outgoing stocks
        """
        domain.append(["picking_type_id", "=", self.env.ref(
            "stock.picking_type_out"
        ).id])
        if self.env.user not in self.env.ref("stock.group_stock_manager").users:
            domain.append(["create_uid", "=", self.env.context["uid"]])
        stock_moves = self.env["stock.move"].search(domain)
        delivery_orders, products = [], []
        for product in stock_moves.mapped("product_id").filtered(
                lambda r: r.detailed_type == "product"
        ):
            quantity = 0
            for rec in stock_moves.filtered(lambda r: r.product_id == product):
                quantity += rec.product_uom_qty
            products.append(product.name)
            delivery_orders.append(quantity)
        return {
            "labels": products,
            "data": delivery_orders,
        }

    def get_internal_transfer(self, domain):
        """
        To get internal transfers
        """
        domain.append(["picking_type_id", "=", self.env.ref(
            "stock.picking_type_internal"
        ).id])
        if self.env.user not in self.env.ref("stock.group_stock_manager").users:
            domain.append(["create_uid", "=", self.env.context["uid"]])
        stock_moves = self.env["stock.move"].search(domain)
        internal_transfers, products = [], []
        for product in stock_moves.mapped("product_id").filtered(
                lambda r: r.detailed_type == "product"
        ):
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
        if self.env.user not in self.env.ref("stock.group_stock_manager").users:
            domain.append(["create_uid", "=", self.env.context["uid"]])
        purchase_order_lines = self.env["purchase.order.line"].search(domain)
        average_expense, products, quantities = [], [], []
        for product in purchase_order_lines.mapped("product_id").filtered(
                lambda r: r.detailed_type == "product"
        ):
            price_subtotal = 0
            quantity = 0
            for rec in purchase_order_lines.filtered(
                    lambda r: r.product_id == product and
                              r.qty_received > 0
            ):
                quantity += rec.qty_received
                price_subtotal += rec.qty_received * rec.price_unit
            if price_subtotal > 0 and quantity > 0:
                products.append(product.name)
                quantities.append(product.qty_available)
                average_expense.append(price_subtotal / quantity)
        return {
            "labels": products,
            "data": average_expense,
            "qty_available": quantities,
        }

    def get_inventory_valuation(self, domain):
        """
        To get datas for inventory valuation
        """
        result = self.get_average_expense(domain)
        return {
            "labels": result["labels"],
            "data": [(result["data"][i] * result["qty_available"][i]) for i in
                     range(len(result["labels"]))]
        }

    def get_stock_location(self):
        """
        To get warehouse location based stock
        """
        stock_quant_ids = self.env["stock.quant"].sudo().search([
            ("location_id.usage", "=", "internal"),
            ("company_id", "=", self.env.context["allowed_company_ids"][0])
        ])
        quantities = []
        for record in stock_quant_ids.mapped("location_id"):
            quantity = 0
            for rec in stock_quant_ids.filtered(
                    lambda r: r.location_id == record
            ):
                quantity += rec.inventory_quantity_auto_apply
            quantities.append(quantity)
        return {
            "labels": [(i.location_id.name + "/" + i.name) for i in
                       stock_quant_ids.mapped("location_id")],
            "data": quantities,
        }

    def get_stock_move(self):
        """
        To get total stock moves of warehouse
        """
        picking_types = self.env["stock.picking.type"].search([])
        transfers = []
        for picking_type in picking_types:
            transfers.append(
                self.env["stock.picking"].search_count([
                    ("picking_type_id", "=", picking_type.id)
                ])
            )
        return {
            "labels": [i.name for i in picking_types],
            "data": transfers,
        }
