# -*- coding: utf-8 -*-
from odoo import api, fields, models

# Global variables
_product_id_old = []


class SaleOrder(models.Model):
    """
    To inherit sales order page.
    """
    _inherit = "sale.order"

    associated_products = fields.Boolean(
        string="Associated Products", help="Check to add associated products")

    # Onchange Functions

    @api.onchange("associated_products", "partner_id")
    def _onchange_associated_products(self):
        """
        To add records in sale order lines.
        """
        for record in self.order_line:
            if record.product_id.id in _product_id_old:
                self.update({
                    'order_line': [(fields.Command.unlink(record.id))]
                })
        _product_id_old.clear()
        if self.partner_id.associated_product_ids:
            if self.associated_products:
                for product in self.partner_id.associated_product_ids:
                    _product_id_old.append(product.id)
                    vals = {
                        "product_id": product.id,
                        "product_uom_qty": 1,
                        "product_uom": product.uom_id,
                        "price_unit": product.list_price,
                        "name": product.name,
                        "order_id": self.id,
                    }
                    self.update({
                        'order_line': [(fields.Command.create(vals))],
                    })
            else:
                for record in self.order_line:
                    if record.product_id.id \
                            in [product.id for product in
                                self.partner_id.associated_product_ids]:
                        self.update({
                            'order_line': [(fields.Command.unlink(record.id))]
                        })
