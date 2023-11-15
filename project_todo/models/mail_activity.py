# -*- coding: utf-8 -*-
from odoo import models


class MailActivity(models.Model):
    """
    To inherit mail acitiviy
    """
    _inherit = 'mail.activity'

    def _action_done(self, feedback=False, attachment_ids=None):
        """
        To change the status
        """
        if self.res_model == "todo.task":
            task = self.env["todo.task"].browse(self.res_id)
            task.stage = "done"
        result = super(MailActivity, self)._action_done(
            feedback=False, attachment_ids=None
        )
        return result
    