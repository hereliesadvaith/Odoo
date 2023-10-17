# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProjectTemplate(models.Model):
    """
    To create project template model
    """
    _name = "project.template"
    _description = "Project Template"

    name = fields.Char("Name", help="name", required=True)
    label_tasks = fields.Char("Name of the tasks", help="Label of tasks")
    tag_ids = fields.Many2many("project.tags", string="Tags",
                               help="Tags")
    company_id = fields.Many2one("res.company", string="Company",
                                 help="Company")
    user_id = fields.Many2one("res.users", string="Project Manager",
                              help="Project Manager")

    # Action Methods

    def action_create_project(self):
        """
        To create a project using template
        """
        return {
            "type": "ir.actions.act_window",
            "res_model": "project.project",
            "name": "Create Project",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_label_tasks": self.label_tasks,
                "default_tag_ids": self.tag_ids.ids,
                "default_company_id": self.company_id.id,
                "default_user_id": self.user_id.id,
            }
        }
