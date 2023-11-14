# -*- coding: utf-8 -*-
from odoo import api, fields, models
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
    state = fields.Selection(selection=[
        ("today", "Today"),
        ("planned", "Planned"),
        ("expired", "Expired"),
        ("done", "Done")
    ], string="Status", help="Status", tracking=True, default="today",
    compute="_compute_state")
    stage = fields.Selection(selection=[
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
    due_date = fields.Date("Due Date", help="Due date",
                           default=fields.Date.today())
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
    
    @api.depends("activity_ids")
    def _compute_state(self):
        """
        To compute the stage of the todo task
        """
        for record in self:
            if record.activity_ids:
                record.stage = "today"
                record.state = "today"
            else:
                record.stage = "done"
                record.state = "done"
            if record.due_date > fields.Date.today():
                record.stage = "planned"
                record.stage = "planned"
            if record.due_date < fields.Date.today():
                record.stage = "expired"
                record.state = "expired"

    # Onchange & Constrains 

    @api.constrains("activity_type_id", "due_date", "description")
    def _check_activity_type_id(self):
        """
        To check activity type
        """
        if self.activity_type_id:
            if self.activity_ids:
                self.update({
                    "activity_ids": [fields.Command.update(
                        self.activity_ids[0].id, {
                            "activity_type_id": self.activity_type_id.id,
                            "summary": self.summary,
                            "date_deadline": self.due_date,
                        })]
                })
            else:
                self.update({
                    "activity_ids": [fields.Command.create({
                        "activity_type_id": self.activity_type_id.id,
                        "summary": self.summary,
                        "user_id": self.user_id.id,
                        "date_deadline": self.due_date,
                        "res_model_id": self.res_model.id,
                        "res_id": self.id,
                    })]
                })
            