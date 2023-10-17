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
    project_template_id = fields.Many2one("project.template",
                                          help="Project template id")

    # Action Methods

    def action_create_task(self):
        """
        To create task using template
        """
        return {
            "type": "ir.actions.act_window",
            "res_model": "project.task",
            "name": "Create Template",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_name": self.name,
                "default_user_ids": self.user_ids.ids,
                "default_tag_ids": self.tag_ids.ids,
            }
        }
