# -*- coding: utf-8 -*-
from odoo import fields, models


class FrequentProduct(models.Model):
    """
    Model for frequent products
    """
    _name = "frequent.product"
    _description = "Frequent Product"

    res_partner_id = fields.Many2one("res.partner", help="Parnter")
    product_id = fields.Many2one("product.product",
                                 string="Product", help="Product")
    sale_orders = fields.Integer("No of Sale Orders",
                                 help="No of sale orders for the product")
    last_sale_date = fields.Date("Recent Sale Date",
                                 help="Recent sale date for the product")
    last_invoiced_amount = fields.Float("Last Invoiced Amount",
                                        help="Last invoiced amount for the product")
    