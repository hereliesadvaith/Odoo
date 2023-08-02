# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    """
    To add fields in invoice page.
    """
    _inherit = "sale.order"

    # CRUD functions

    def merge_lines(self, res):
        """
        To merge sale order lines with same product
        """
        product_id_list = []
        for record in self.order_line:
            if [record.product_id, record.price_unit] in [[i[1], i[2]] for i in product_id_list]:
                for i in product_id_list:
                    if (record.product_id == i[1]) and (
                            i[0].price_unit == record.price_unit):
                        i[0].product_uom_qty += record.product_uom_qty
                        self.update({
                            'order_line': [(fields.Command.delete(record.id))]
                        })
            else:
                product_id_list.append([record, record.product_id, record.price_unit])
        product_id_list.clear()

    @api.model
    def create(self, vals):
        """
        Call our function when creating new record.
        """
        res = super(SaleOrder, self).create(vals)
        res.merge_lines(res)
        return res

    @api.model
    def write(self, vals):
        """
        Call function when updating a record
        """
        res = super(SaleOrder, self).write(vals)
        self.merge_lines(self)
        return res
