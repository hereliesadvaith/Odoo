# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PurchaseOrder(models.Model):
    """
    To inherit purchase order
    """
    _inherit = "purchase.order"

    supplier_ids = fields.One2many("supplier.info",
                                   "purchase_order_id")

    # CRUD Methods

    @api.constrains("order_line")
    def _create_supplier_info(self):
        for order in self.order_line:
            for record in order.product_id.seller_ids:
                if record.partner_id != self.partner_id:
                    self.update({
                        "supplier_ids": [(fields.Command.create({
                            "product_id": order.product_id.id,
                            "vendor_id": record.partner_id.id,
                            "product_qty": order.product_qty,
                            "price": record.price
                        }))]
                    })

    # Action Methods

    def action_check_price(self):
        """
        To open the wizard.
        """
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'compare.price',
            'name': 'Compare Price',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_supplier_ids': [(
                    fields.Command.link(i)) for i in self.supplier_ids.ids],
            }
        }
