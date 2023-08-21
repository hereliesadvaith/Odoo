# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    """
    To inherit sale order page.
    """
    _inherit = "sale.order"

    # Action Methods

    def action_confirm(self):
        """
        To create a purchase order
        """
        result = super(SaleOrder, self).action_confirm()
        for order in self.order_line:
            if order.product_id.seller_ids:
                purchase_order = self.env["purchase.order"].create({
                    "partner_id": order.product_id.seller_ids[0].partner_id.id,
                    "origin": self.name,
                    "order_line": [(fields.Command.create({
                        "product_id": order.product_id.id,
                        "product_qty": order.product_uom_qty,
                        "price_unit": order.price_unit,
                    }))],
                })
                purchase_order.button_confirm()
        return result
