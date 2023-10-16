# -*- coding: utf-8 -*-
from odoo import api, fields, models


class TaskTemplate(models.Model):
    """
    To create task template model
    """
    _name = "task.template"
    _description = "Task Template"

    name = fields.Char("Name", help="name")
