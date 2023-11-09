# -*- coding: utf-8 -*-
from odoo import api, fields, models
import datetime
from dateutil.relativedelta import relativedelta


class ResPartner(models.Model):
    """
    To add fields in contact form.
    """
    _inherit = "res.partner"

    associated_product_ids = fields.Many2many(
        "product.product", help="Associated products")
    
    frequent_product_ids = fields.One2many("frequent.product", "res_partner_id",
                                           compute="_compute_frequent_product_ids",help="Frequent products")

    def new_print(*args):
        print("\033[33m")
        print(args[-1])
        print("\033[0m")

    # Compute Methods

    def _compute_frequent_product_ids(self):
        """
        To add values to one2many field
        """
        for record in self:
            record.frequent_product_ids = False
            domain = [("partner_id", "=", record.id), ("invoice_status", "=", "invoiced")]
            no_of_months = self.env['ir.config_parameter'].sudo().get_param(
            'no_of_months'
            )
            limit = self.env['ir.config_parameter'].sudo().get_param(
            'select_limit'
            )
            if int(no_of_months) > 0:
                end_date = datetime.date.today() - relativedelta(months=int(no_of_months))
                domain.append(("date_order", ">", end_date))
            sale_order_ids = self.env['sale.order'].search(
                domain, order="date_order DESC"
            )
            order_lines = self.env["sale.order.line"].search([
                ("order_id", "in", sale_order_ids.ids)
            ])
            for product in order_lines.mapped("product_id"):
                frequent_product_data = {"res_partner_id": record.id}
                frequent_product_data["product_id"] = product.id
                sale_orders = []
                last_sale_date = False
                last_invoiced_amount = False
                for order_line in order_lines.filtered(
                    lambda r: r.product_id == product
                ):
                    if order_line.order_id not in sale_orders:
                        sale_orders.append(order_line.order_id)
                    if not last_sale_date:
                        last_sale_date = order_line.order_id.date_order
                    if not last_invoiced_amount:
                        last_invoiced_amount = order_line.price_subtotal
                frequent_product_data["sale_orders"] = len(sale_orders)
                frequent_product_data["last_sale_date"] = last_sale_date
                frequent_product_data["last_invoiced_amount"] = last_invoiced_amount
                self.new_print(frequent_product_data)
                self.env["frequent.product"].create(frequent_product_data)
