# -*- coding: utf-8 -*-

from odoo import fields, models


class ComponentRequest(models.Model):
    """
    This class is used to make the model of our Request For Warranty page
    """
    _name = "component.request"
    _description = "Component Request"

    name = fields.Char(string="Name")
    user_id = fields.Many2one("res.users", string="Responsible")
    order_line_ids = fields.One2many("component.order.line", "order_id")
