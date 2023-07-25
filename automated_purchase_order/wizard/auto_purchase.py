# -*- coding: utf-8 -*-

from odoo import fields, models


class AutoPurchase(models.TransientModel):
    """
    Model for wizard
    """
    _name = "auto.purchase"
    _description = "Auto Purchase"

    name = fields.Char(string="Name")
    note = fields.Text(string="Notes")
