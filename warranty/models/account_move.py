# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductsTemplate(models.Model):
    """
    To add fields in invoice page.
    """

    _inherit = "account.move"
    warranty_ids = fields.One2many("request.for.warranty",
                                   inverse_name="invoice_id",
                                   readonly=True)
