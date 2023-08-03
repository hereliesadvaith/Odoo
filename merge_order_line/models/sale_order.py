# -*- coding: utf-8 -*-
from odoo import models, api


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
            if ([i[2]["product_id"], i[2]["price_unit"]]
                    in [[i[0], i[2]] for i in product_id_list]):
                for j in product_id_list:
                    if (i[2]["product_id"] == j[0]) and (
                            i[2]["price_unit"] == j[2]):
                        j[1] += i[2]["product_uom_qty"]
            else:
                product_id_list.append(
                    [i[2]["product_id"], i[2]["product_uom_qty"], i[2][
                        "price_unit"]])
        order_line_copy = []
        for j in product_id_list:
            for i in vals["order_line"]:
                if (j[0] == i[2]["product_id"]) and (
                        j[2] == i[2]["price_unit"]):
                    if [i[2]["product_id"], i[2]["price_unit"]] not in [
                        [k[2]["product_id"], k[2][
                            "price_unit"]] for k in order_line_copy]:
                        i[2]["product_uom_qty"] = j[1]
                        order_line_copy.append(i)
        vals["order_line"] = order_line_copy
        res = super(SaleOrder, self).create(vals)
        return res
