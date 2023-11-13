# -*- coding: utf-8 -*-
from odoo import fields, models


class TodoTask(models.Model):
    """
    To create model for To-Do tasks.
    """
    _name = "todo.task"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "To-Do Task"

    name = fields.Char("Task", help="Task name")
    user_id = fields.Many2one("res.users", help="User id",
                              default = lambda self: self.env.user)
    tag_ids = fields.Many2many("product.product", help="Task tags")
    state = fields.Selection(selection=[
        ("today", "Today"),
        ("planned", "Planned"),
        ("expired", "Expired"),
        ("done", "Done")
    ], string="Status", help="Status", tracking=True)
    description = fields.Html(string="Description", sanitize_attributes=False)
    priority = fields.Selection([
        ("0", "Low"),
        ("1", "High"),
        ("2", "Urgent")
    ], default="0", string="Priority", tracking=True, help="Priority")
