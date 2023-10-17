# -*- coding: utf-8 -*-
from odoo import api, fields, models


class TaskTemplate(models.Model):
    """
    To create task template model
    """
    _name = "task.template"
    _description = "Task Template"

    name = fields.Char("Name", help="name")
    user_ids = fields.Many2many("res.users", string="Assignees",
                                help="Assignees")
    tag_ids = fields.Many2many("project.tags", string="Tags",
                               help="Tags")

    # Action Methods

    def action_create_task(self):
        """
        To create task using template
        """
        print("hi")
