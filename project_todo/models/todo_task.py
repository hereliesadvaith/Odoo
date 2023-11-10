# -*- coding: utf-8 -*-
from odoo import fields, models


class TodoTask(models.Model):
    """
    To create model for To-Do tasks.
    """
    _name = "todo.task"
    _description = "To-Do Task"

    name = fields.Char("Task")
    tag_ids = fields.Many2many("product.product")
    