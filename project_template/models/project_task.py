# -*- coding: utf-8 -*-
from odoo import models


class ProjectTask(models.Model):
    """
    To inherit project model
    """
    _inherit = "project.task"

    # Action Methods
    def action_create_template(self):
        """
        To create task template
        """
        return {
            "type": "ir.actions.act_window",
            "res_model": "task.template",
            "name": "Create Template",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_name": "hello there",
            }
        }
