# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductProduct(models.Model):
    """
    To add fields to product template model.
    """
    _inherit = ["product.product"]

    sale_count = fields.Integer(
        "Total Sale count", compute="_compute_sale_count")

    # Compute Methods

    def _compute_sale_count(self):
        """
        To compute sale count
        """
        for record in self:
            sale_order_lines = self.env["sale.order.line"].search([(
                "product_id", "=", record.id)])
            record.sale_count = len(sale_order_lines)

    # Onchange functions

    @api.onchange("lst_price")
    def _onchange_lst_price(self):
        """
        To change price in draft sale orders
        """
        sale_order_lines = self.env["sale.order.line"].search([
            ("product_id", "=", self._origin.id),
            ("state", "=", "draft"),
        ])
        for order in sale_order_lines:
            order.price_unit = self.lst_price
