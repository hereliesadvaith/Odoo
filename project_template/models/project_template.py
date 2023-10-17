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
    task_template_ids = fields.One2many("task.template",
                                        "project_template_id",
                                        help="Tasks")
    task_stage_ids = fields.Many2many("project.task.type",
                                      string="Task Stages",
                                      help="Task Stages")

    # Action Methods

    def action_create_project(self):
        """
        To create a project using template
        """
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": "create.template",
            "name": "Create Form",
            "view_mode": "form",
            "target": "new",
            "context": {
                "label_tasks": self.label_tasks,
                "tag_ids": self.tag_ids.ids,
                "company_id": self.company_id.id,
                "user_id": self.user_id.id,
                "task_template_ids": self.task_template_ids.ids,
                "task_stage_ids": self.task_stage_ids.ids,
            },
        }
