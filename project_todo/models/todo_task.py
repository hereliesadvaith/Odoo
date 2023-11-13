# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.tools import html2plaintext


class TodoTask(models.Model):
    """
    To create model for To-Do tasks.
    """
    _name = "todo.task"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "To-Do Task"
    _rec_name = "summary"

    user_id = fields.Many2one("res.users", help="User id",
                              default = lambda self: self.env.user)
    stage_id = fields.Many2one("todo.stage", help="Todo stages")
    tag_ids = fields.Many2many("todo.tag", string="Tags", help="Todo tags")
    state = fields.Selection(selection=[
        ("today", "Today"),
        ("planned", "Planned"),
        ("expired", "Expired"),
        ("done", "Done")
    ], string="Status", help="Status", tracking=True, default="today")
    description = fields.Html(string="Description", help="Description")
    priority = fields.Selection([
        ("0", "None"),
        ("1", "Low"),
        ("2", "High"),
        ("3", "Urgent")
    ], default="0", string="Priority", tracking=True, help="Priority")
    due_date = fields.Date("Due Date", help="Due date")
    recurring = fields.Boolean(string="Recurring", store=True, help="Recurring task")
    interval = fields.Selection(
        [('Daily', 'Daily'),
         ('Weekly', 'Weekly'),
         ('Monthly', 'Monthly'),
         ('Quarterly', 'Quarterly'),
         ('Yearly', 'Yearly')],
        string='Recurring Interval', )
    new_date = fields.Date(string="Next Due Date", store=True)
    res_model = fields.Many2one("ir.model", string="Model of todo task",
                                   default=lambda self: self.env.ref(
                                       "project_todo.model_todo_task"
                                   ))
    activity_type_id = fields.Many2one("mail.activity.type",
                                       string="Activity Type",
                                       help="Activity Type", store=True)
    summary = fields.Char("Summary", help="Summary", compute="_compute_summary")


    # Compute Methods

    def _compute_summary(self):
        """
        To compute name from description's first line
        """
        for todo in self:
            if todo.summary:
                continue
            text = html2plaintext(todo.description) if todo.description else "New"
            todo.summary = text.strip().replace('*', '').split("\n")[0]
            