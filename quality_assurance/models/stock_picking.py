# -*- coding: utf-8 -*-
from odoo import fields, models, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    """
    To add functions inside Stock Picking model.
    """
    _inherit = "stock.picking"

    quality_alert_count = fields.Integer("Alert Count", compute="_compute_quality_alert", default=0)

    # Compute Methods

    def _compute_quality_alert(self):
        """
        To compute alert count
        """
        for record in self:
            quality_alerts = self.env['quality.alert'].search_count(
                [("stock_picking_id", "=", record.id)])
            record.quality_alert_count = quality_alerts

    # Action Methods

    def action_quality_alert(self):
        """
        To show quality alerts
        """
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Quality Alerts",
            "view_mode": "tree,form",
            "res_model": "quality.alert",
            "context": "{'create': False}",
            "domain": [("stock_picking_id", "=", self.id)],
        }

    def generate_quality_alert(self):
        """
        To generate quality alerts
        """
        for record in self.move_ids:
            quality_measure_ids = self.env["quality.measure"].search([
                ("product_id", "=", record.product_id.id),
                ("trigger_ids", "in", self.picking_type_id.id)
            ])
            if quality_measure_ids:
                self.env["quality.alert"].create({
                    "product_id": record.product_id.id,
                    "stock_picking_id": self.id,
                })
    
    def action_confirm(self):
        """
        To crete quality alerts on action confirm
        """
        self.ensure_one()
        res = super(StockPicking, self).action_confirm()
        self.generate_quality_alert()
        return res
    
    def button_validate(self):
        """
        Check quality alert status
        """
        self.ensure_one()
        if self.quality_alert_count > 0:
            quality_alert_ids = self.env['quality.alert'].search(
                [("stock_picking_id", "=", self.id)])
            for quality_alert_id in quality_alert_ids:
                if quality_alert_id.state != "pass":
                    raise UserError("There are unresolved Quality Checks")
        res = super(StockPicking, self).button_validate()
        return res
    