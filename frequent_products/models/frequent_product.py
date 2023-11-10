# -*- coding: utf-8 -*-
from odoo import fields, models


class FrequentProduct(models.Model):
    """
    Model for frequent products
    """
    _name = "frequent.product"
    _description = "Frequent Product"

    partner_id = fields.Many2one("res.partner", help="Parnter")
    order_id = fields.Many2one("sale.order", help="Sale Order")
    product_id = fields.Many2one("product.product",
                                 string="Product", help="Product")
    sale_orders = fields.Integer("No of Sale Orders",
                                 help="No of sale orders for the product")
    last_sale_date = fields.Date("Recent Sale Date",
                                 help="Recent sale date for the product")
    last_invoiced_amount = fields.Float("Last Invoiced Amount",
                                        help="Last invoiced amount for the product")

    # Action Methods

    def action_add_product(self):
        """
        To add product to order line
        """
        self.ensure_one()
        if self.product_id.id in self.order_id.order_line.mapped(
            "product_id").ids:
            order_line = self.order_id.order_line.filtered(
                lambda r: r.product_id == self.product_id
            )[0]
            order_line.write({
                "product_uom_qty": order_line.product_uom_qty + 1,
            })
        else:
            self.order_id.update({
                "order_line": [(fields.Command.create({
                    "product_id": self.product_id.id,
                    "product_uom_qty": 1,
                    "price_unit": self.product_id.list_price,
                    "name": self.product_id.name,
                    "order_id": self.order_id.id,
                }))]
            })
