# -*- coding: utf-8 -*-
from odoo import fields, models


class CreateTemplate(models.TransientModel):
    """
    Model for wizard
    """
    _name = "create.template"
    _description = "Create Template"

    name = fields.Char("Name", help="Name", required=True)

    def action_confirm(self):
        """
        To create projects and templates
        """
        context = self.env.context
        match context["active_model"]:
            case "project.project":
                task_ids = self.env["project.task"].search([
                    ("project_id", "=", context['active_id'])
                ])
                task_template_ids = []
                for task in task_ids:
                    task_template_id = self.env["task.template"].create({
                        "name": task.name,
                        "user_ids": task.user_ids.ids,
                        "tag_ids": task.tag_ids.ids,
                    })
                    task_template_ids.append(task_template_id.id)
                stage_ids = self.env["project.task.type"].search([
                    ("project_ids", "in", [context['active_id']])
                ])
                project_template = self.env["project.template"].create({
                    "name": self.name,
                    "label_tasks": context['label_tasks'],
                    "tag_ids": context['tag_ids'],
                    "company_id": context['company_id'],
                    "user_id": context['user_id'],
                    "task_template_ids": task_template_ids,
                    "task_stage_ids": stage_ids.ids,
                })
                return project_template
            case "project.template":
                project = self.env["project.project"].create({
                    "name": self.name,
                    "label_tasks": context['label_tasks'],
                    "tag_ids": context['tag_ids'],
                    "company_id": context['company_id'],
                    "user_id": context['user_id'],
                })
                task_stage_ids = self.env["project.task.type"].browse(
                    context['task_stage_ids']
                )
                for task_stage in task_stage_ids:
                    task_stage.update({
                        'project_ids': [(fields.Command.link(project.id))]
                    })
                task_template_ids = self.env["task.template"].browse(
                    context['task_template_ids']
                )
                for task_template in task_template_ids:
                    self.env["project.task"].create({
                        "name": task_template.name,
                        "project_id": project.id,
                        "tag_ids": task_template.tag_ids.ids,
                        "user_ids": task_template.user_ids.ids,
                    })
