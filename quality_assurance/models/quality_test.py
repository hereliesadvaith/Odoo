# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class QualityTest(models.Model):
    """
    Model for Quality Tests.
    """
    _name = "quality.test"
    _description = "Quality Test"

    name = fields.Char(readonly=True, help="Name of quality test")
    test_type = fields.Selection(selection=[
        ("quantity", "Quantitative"),
        ("quality", "Qualitative")
    ], string="Test Type", help="Test type", default="quantity")
    state = fields.Selection(selection=[
        ("ongoing", "Ongoing"),
        ("pass", "Pass"),
        ("fail", "Fail")
    ], string="Status", help="Status")
    quality_measure_id = fields.Many2one("quality.measure", string="Measure",
                                         help="Measure")
    quality_alert_id = fields.Many2one("quality.alert", string="Alert",
                                       help="Quality alert")
    product_id = fields.Many2one("product.product", string="Product",
                                 help="Product")
    user_id = fields.Many2one("res.users", string="Assigned To",
                              help="Assigned to")
    status = fields.Selection(selection=[
        ("ongoing", "Ongoing"),
        ("pass", "Pass"),
        ("fail", "Fail")
    ], string="Status", default="ongoing")
    quantitative_result = fields.Integer("Quantitative Result",
                                         help="Result")
    qualitative_result = fields.Selection(selection=[
        ("satisfied", "Satisfied"),
        ("unsatisfied", "Unsatisfied")
    ], string="Qualitative Result", help="Result")
    

    # Onchange Methods

    @api.onchange("quantitative_result", "qualitative_result")
    def onchange_result(self):
        """
        To change the status of quality test
        """
        if self.test_type == "quality":
            print("hii")
            if self.qualitative_result == "satisfied":
                self.status = "pass"
            elif self.qualitative_result == "unsatisfied":
                self.status = "fail"
            else:
                self.status = "ongoing"
        else:
            demand_qty = self.quality_alert_id.stock_picking_id.move_ids.filtered(
                lambda r: r.product_id == self.quality_alert_id.product_id
                )[0].product_uom_qty
            print(demand_qty)
            if self.quantitative_result >= demand_qty:
                self.status = "pass"
            else:
                self.status = "ongoing"
            