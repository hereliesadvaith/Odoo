# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    def _create_invoices(self, sale_order_ids):
        """
        To inherit create_invoices
        """
        result = super(
            SaleAdvancePaymentInv, self)._create_invoices(sale_order_ids)
        for order_line in result.line_ids.sale_line_ids:
            for line in result.line_ids.filtered(
                lambda r: r.product_id == order_line.product_id and
                r.sale_line_ids != order_line
            ):
                line.sale_line_ids += order_line
        for line in result.line_ids.filtered(
            lambda r: r.product_id
        ):
            if line.id in result.line_ids.ids:
                invoice_lines = result.line_ids.filtered(
                    lambda r: r.product_id == line.product_id and
                    r.price_unit == line.price_unit
                )
                quantity = 0
                unit_price = invoice_lines[0].price_unit
                for invoice_line in invoice_lines:
                    quantity += invoice_line.quantity
                invoice_lines[0].quantity = quantity
                invoice_lines[0].price_unit = unit_price
                invoice_lines[1:].unlink()
        for line in result.line_ids:
            line.sale_order_names = ', '.join([i.name for i in line.sale_line_ids.order_id])
        return result
