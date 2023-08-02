# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    """
    To add fields in invoice page.
    """
    _inherit = "sale.order"

    # CRUD functions

    @api.model
    def merge_lines(self, vals):
        """
        To merge sale order lines with same product
        """
        product_id_list = []
        for record in self.order_line:
            if record.product_id in [i[1] for i in product_id_list]:
                for i in product_id_list:
                    if (record.product_id == i[1]) and (
                            i[0].price_unit == record.price_unit):
                        i[0].product_uom_qty += record.product_uom_qty
                        self.update({
                            'order_line': [(fields.Command.delete(record.id))]
                        })
            else:
                product_id_list.append([record, record.product_id])
        product_id_list.clear()
