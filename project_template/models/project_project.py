# -*- coding: utf-8 -*-
from odoo import models


class ProjectProject(models.Model):
    """
    To inherit project model
    """
    _inherit = "project.project"

    # Action Methods
    def action_create_template(self):
        """
        To create project template
        """
        return {
            "type": "ir.actions.act_window",
            "res_model": "project.template",
            "name": "Create Template",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_name": "hi there",
            }
        }
