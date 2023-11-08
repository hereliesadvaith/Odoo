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
    state = fields.Selection(selection=[
        ("ongoing", "Ongoing"),
        ("pass", "Pass"),
        ("fail", "Fail")
    ], string="Status")
    quantitative_result = fields.Integer("Result")
    qualitative_result = fields.Selection(selection=[
        ("satisfied", "Satisfied"),
        ("unsatisfied", "Unsatisfied")
    ], string="Result")
    