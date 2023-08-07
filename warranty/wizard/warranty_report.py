# -*- coding: utf-8 -*-
from odoo import models, fields


class WarrantyReportWizard(models.TransientModel):
    """
    Model for wizard
    """
    _name = "warranty.report.wizard"
    _description = "Warranty Report Wizard"

    product_ids = fields.Many2many("product.product",
                                   string="Product",
                                   help="Product")
    partner_id = fields.Many2one("res.partner")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    # Action methods

    def action_confirm(self):
        """
        To print the pdf report the report
        """
        domain = []
        if self.start_date:
            domain += [('request_date', '>=', self.start_date)]
        if self.end_date:
            domain += [('request_date', '<=', self.end_date)]
        if self.product_ids:
            domain += [('product_id', 'in', [i.id for i in self.product_ids])]
        if self.partner_id:
            domain += [('customer_id', '=', self.partner_id.id)]
        warranties = self.env["request.for.warranty"].search_read(domain)
        data = {
            'warranties': warranties
        }
        return self.env.ref('warranty.warranty_report_action').report_action(
            None, data=data)
