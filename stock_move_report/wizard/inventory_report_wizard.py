# -*- coding: utf-8 -*
from odoo import fields, models
from odoo.exceptions import ValidationError


class InventoryReportWizard(models.TransientModel):
    """
    Model for inventory report wizard
    """
    _name = "inventory.report.wizard"
    _description = "Inventory Report Wizard"

    product_ids = fields.Many2many("product.product", string="Products",
                                 help="Select Products")
    location_ids = fields.Many2many("stock.location", string="Locations",
                                    help="Select Locations")
    state = fields.Selection(selection=[
            ("draft", "Draft"),
            ("waiting", "Waiting Another Operation"),
            ("confirmed", "Waiting"),
            ("assigned", "Ready"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
        ],
        help="Status", string="Status")
    start_date = fields.Date(string="Start Date", help="Start Date")
    end_date = fields.Date(string="End Date", help="End Date")

    # Action Methods

    def print_pdf(self):
        """
        To print pdf report
        """
        company_id = self.env.context['allowed_company_ids'][0]
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError("Set valid period")
        query = f"""
        SELECT * FROM stock_move_line as sml
        WHERE sml.company_id = {company_id}
        """
        self.env.cr.execute(query)
        stock_moves = self.env.cr.dictfetchall()
        result = {
            "data": stock_moves,
        }
        return self.env.ref("stock_move_report.inventory_report_action").report_action(
            None, data=result
        )

    def print_xlsx(self):
        """
        To print xlsx report
        """
        print("xlsx")