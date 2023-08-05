# -*- coding: utf-8 -*-
from odoo import fields, models


class WarrantyReport(models.TransientModel):
    """
    Model for wizard
    """
    _name = "warranty.wizard"
    _description = "Warranty Report"

    product_ids = fields.Many2many("product.product",
                                   string="Product",
                                   help="Product")
    partner_id = fields.Many2one("res.partner")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    warranty_id = fields.Many2one("request.for.warranty")

    # Action methods

    def action_confirm(self):
        """
        To print the pdf report the report
        """
        pass
