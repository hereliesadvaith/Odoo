# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime


class QualityAlert(models.Model):
    """
    Model for Quality Alert.
    """
    _name = "quality.alert"
    _description = "Quality Alert"

    name = fields.Char(
        readonly=True,
        default=lambda self: _("New"),
        copy=False,
        help="Sequence number of quality alert"
    )
    product_id = fields.Many2one("product.product", string="Product",
                                 required=True, help="Product")
    user_id = fields.Many2one("res.users", string="Created By",
                              help="Created by",
                              default=lambda self: self.env.uid)
    date = fields.Date("Date", default=datetime.now(),
                       help="Created date")
    stock_picking_id = fields.Many2one("stock.picking",
                                       string="Source Operation",
                                       )
    state = fields.Selection(store=True, selection=[
        ("ongoing", "Ongoing"),
        ("pass", "Pass"),
        ("fail", "Fail")
    ], string="Status", default="ongoing", compute="_compute_state")
    quality_test_ids = fields.One2many("quality.test", "quality_alert_id",
                                       help="Quality Tests")
    is_test_generated = fields.Boolean("is_test_generated", default=False)
    
    # Action Methods

    def action_generate_test(self):
        """
        To generate quality tests
        """
        self.ensure_one()
        quality_measuere_ids = self.env["quality.measure"].search([
            ("product_id", "=", self.product_id.id),
            ("trigger_ids", "in", self.stock_picking_id.picking_type_id.id)
        ])
        for quality_measure_id in quality_measuere_ids:
            self.update({
                "quality_test_ids": [(fields.Command.create({
                    "name": quality_measure_id.name,
                    "test_type": quality_measure_id.test_type,
                    "quality_measure_id": quality_measure_id.id,
                    "quality_alert_id": self.id,
                    "product_id": self.product_id.id,
                }))]
            })
        self.is_test_generated = True
    
    @api.depends("quality_test_ids")
    def _compute_state(self):
        """
        To compute status of the alert
        """
        for record in self:
            if record.quality_test_ids:
                if len(record.quality_test_ids) == len(
                    record.quality_test_ids.filtered(
                        lambda r: r.status == "pass")):
                    self.state = "pass"
                else:
                    self.state = "ongoing"
            else:
                self.state ="ongoing"

    
    # CRUD Methods

    @api.model_create_multi
    def create(self, vals_list):
        """
        Used to create sequence number for quality alert.
        """
        for vals in vals_list:
            if vals.get("name", _("New")) == _("New"):
                vals["name"] = self.env["ir.sequence"].next_by_code(
                    "quality.alert.sequence"
                ) or _("New")
        result = super(QualityAlert, self).create(vals_list)
        return result
    