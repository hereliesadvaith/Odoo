# -*- coding: utf-8 -*-
from odoo import fields, models


class TodoTag(models.Model):
    """
    Model for task tags.
    """
    _name = "todo.tag"
    _description = "Todo Tag"

    _sql_constraints = [
        ("name_uniq", "unique (name)", "Tag name already exists !"),
    ]

    name = fields.Char("Tag Name", required=True, help="Name")
    color = fields.Integer("Color Index", help="Color")
