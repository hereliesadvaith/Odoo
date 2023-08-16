# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    """
    To save order history
    """
    _name = "order.history"
    _description = "Order History"
    _rec_name = "sale_id"

    sale_id = fields.Many2one("sale.order", "Sale Order")
    partner_id = fields.Many2one("res.partner", string="Partner")
    date = fields.Date("Date")
    salesperson_id = fields.Many2one("res.users", string="Salesperson")
    purchase_order_ids = fields.One2many("purchase.history", "order_history_id")

    # Action methods

    def cron_order_history(self):
        """
        To run the cron job daily for sale orders
        """
        sale_orders = self.env["sale.order"].search([
            ("state", "=", "sale"),
            ("date_order", ">=", fields.Date.today()),
        ])
        for sale_order in sale_orders:
            order_history = self.create({
                "sale_id": sale_order.id,
                "partner_id": sale_order.partner_id.id,
                "date": fields.Date.today(),
                "salesperson_id": sale_order.user_id.id,
            })
            purchase_orders = self.env["purchase.order"].search([
                ("origin", "=", sale_order.name)
            ])
            for order in purchase_orders:
                order_history.update({
                    "purchase_order_ids": [(fields.Command.create({
                        "purchase_id": order.id,
                        "vendor_id": order.partner_id.id,
                    }))]
                })
