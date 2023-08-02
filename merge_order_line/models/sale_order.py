# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    """
    To add fields in invoice page.
    """
    _inherit = "sale.order"

    # CRUD functions

    @api.model
    def create(self, vals):
        """
        To merge sale order lines with same product
        """
        product_id_list = []
        for i in vals["order_line"]:
            if [i[2]["product_id"], i[2]["price_unit"]] in [[i[0], i[2]] for i in product_id_list]:
                for j in product_id_list:
                    if (i[2]["product_id"] == j[0]) and (
                            i[2]["price_unit"] == j[2]):
                        j[1] += i[2]["product_uom_qty"]
            else:
                product_id_list.append(
                    [i[2]["product_id"], i[2]["product_uom_qty"], i[2]["price_unit"]])
        order_line_copy = []
        for j in product_id_list:
            for i in vals["order_line"]:
                if (j[0] == i[2]["product_id"]) and (j[2] == i[2]["price_unit"]):
                    if [i[2]["product_id"], i[2]["price_unit"]] not in [[k[2]["product_id"], k[2]["price_unit"]] for k in order_line_copy]:
                        i[2]["product_uom_qty"] = j[1]
                        order_line_copy.append(i)
        vals["order_line"] = order_line_copy
        product_id_list.clear()
        res = super(SaleOrder, self).create(vals)
        return res

    # def merge_duplicate_product_lines(self, res):
    #     for line in res.order_line:
    #         if line.id in res.order_line.ids:
    #             line_ids = res.order_line.filtered(lambda m: m.product_id.id == line.product_id.id)
    #             quantity = 0
    #             for qty in line_ids:
    #                 quantity += qty.product_uom_qty
    #                 line_ids[0].write({'product_uom_qty': quantity,
    #                 'order_id': line_ids[0].order_id.id})
    #                 line_ids[1:].unlink()

    # @api.model
    # def create(self, vals):
    #     res = super(SaleOrder, self).create(vals)
    #     res.merge_duplicate_product_lines(res)
    #     return res

    # def write(self, vals):
    #     res = super(SaleOrder, self).write(vals)
    #     self.merge_duplicate_product_lines(self)
    #     return res
