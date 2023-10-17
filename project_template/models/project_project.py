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
                "default_label_tasks": self.label_tasks,
                "default_tag_ids": self.tag_ids.ids,
                "default_company_id": self.company_id.id,
                "default_user_id": self.user_id.id,
            }
        }
