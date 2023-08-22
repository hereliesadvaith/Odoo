# -*- coding: utf-8 -*-
from odoo import models, api


class SaleOrder(models.Model):
    """
    To inherit sale order
    """
    _inherit = "sale.order"

    # Constrains

    @api.constrains("order_line")
    def _merge_order_line(self):
        """
        To merge sale order lines with same product
        """
        for order in self.order_line:
            if order.id in self.order_line.ids:
                order_ids = self.order_line.filtered(
                    lambda r: r.product_id == order.product_id and
                    r.price_unit == order.price_unit
                )
                quantity = 0
                unit_price = order_ids[0].price_unit
                for record in order_ids:
                    quantity += record.product_uom_qty
                order_ids[0].product_uom_qty = quantity
                order_ids[0].price_unit = unit_price
                order_ids[1:].unlink()
