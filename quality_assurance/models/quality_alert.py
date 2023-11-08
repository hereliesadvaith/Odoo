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
    state = fields.Selection(selection=[
        ("ongoing", "Ongoing"),
        ("pass", "Pass"),
        ("fail", "Fail")
    ], string="Status")
    
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
    