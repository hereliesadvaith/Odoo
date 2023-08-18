# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    """
    To add fields in customer page.
    """
    _inherit = "res.partner"

    sale_order_ids = fields.One2many("sale.order",
                                     "partner_id",
                                     help="Sale orders")
    product_count = fields.Integer("Products", default=0,
                                   compute="_compute_product_count",
                                   help="Product count")

    # Compute Functions

    def _compute_product_count(self):
        """
        To compute product count
        """
        for record in self:
            if record.sale_order_ids:
                sale_order_lines = self.env["sale.order.line"].search([(
                    "order_id", "in", self.sale_order_ids.ids)])
                for line in sale_order_lines:
                    record.product_count += line.product_uom_qty
            else:
                record.warranty_expire_date = 0

    # Action Methods

    def action_view_products(self):
        """
        To see the products bought by customer
        """
        self.ensure_one()
        sale_order_lines = self.env["sale.order.line"].search([(
            "order_id", "in", self.sale_order_ids.ids)])
        return {
            "type": "ir.actions.act_window",
            "name": "Products",
            "view_mode": "tree",
            "res_model": "product.product",
            "context": "{'create': False}",
            "domain": [(
                "id", "in", [i.product_id.id for i in sale_order_lines])],
        }
