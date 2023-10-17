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
            },
        }
