# -*- coding: utf-8 -*-
from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    """
    To inherit Sale advance payment inv wizard.
    """
    _inherit = 'sale.advance.payment.inv'

    def _create_invoices(self, sale_orders):
        """
        To inherit create_invoices
        """
        result = super(
            SaleAdvancePaymentInv, self)._create_invoices(sale_orders)
        if len(result) == 1:
            for line in result.line_ids:
                line.sale_order_names = line.sale_line_ids.order_id.name
            for order_line in result.line_ids.sale_line_ids:
                for line in result.line_ids.filtered(
                    lambda r: r.product_id == order_line.product_id and
                    r.price_unit == order_line.price_unit and
                    order_line not in r.sale_line_ids and
                    order_line.order_id not in r.sale_line_ids.order_id
                ):
                    line.sale_line_ids += order_line
                    line.sale_order_names += f", {order_line.order_id.name}"
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
            result.line_ids.sale_line_ids.order_id.invoice_status = 'invoiced'
        return result
