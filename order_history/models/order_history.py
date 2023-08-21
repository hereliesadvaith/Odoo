# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    """
    To save order history
    """
    _name = "order.history"
    _description = "Order History"
    _rec_name = "sale_id"

    sale_id = fields.Many2one("sale.order", "Sale Order",
                              help="Sale order")
    partner_id = fields.Many2one("res.partner", string="Partner",
                                 help="partner",
                                 related="sale_id.partner_id")
    date = fields.Date("Date", help="Order date",
                       default=fields.Date.today())
    salesperson_id = fields.Many2one("res.users",
                                     string="Salesperson",
                                     help="Salesperson",
                                     related="sale_id.user_id")
    purchase_order_ids = fields.One2many("purchase.history",
                                         "order_history_id",
                                         help="Purchase orders")

    # Action Methods

    def cron_order_history(self):
        """
        To run the cron job daily for sale orders
        """
        sale_orders = self.env["sale.order"].search([
            ("state", "=", "sale"),
            ("date_order", ">=", fields.Date.today()),
        ]).filtered(
            lambda r: r not in self.search([]).mapped('sale_id'))
        for sale_order in sale_orders:
            order_history = self.create({
                "sale_id": sale_order.id,
            })
            purchase_orders = self.env["purchase.order"].search([
                ("origin", "=", sale_order.name)
            ])
            for order in purchase_orders:
                order_history.update({
                    "purchase_order_ids": [(fields.Command.create({
                        "purchase_id": order.id,
                    }))]
                })
