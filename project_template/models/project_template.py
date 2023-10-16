# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProjectTemplate(models.Model):
    """
    To create project template model
    """
    _name = "project.template"
    _description = "Project Template"

    name = fields.Char("Name", help="name")
