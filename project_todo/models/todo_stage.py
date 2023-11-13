# -*- coding: utf-8 -*-
from odoo import fields, models


class TodoStage(models.Model):
    """
    Model for task stages.
    """
    _name = "todo.stage"
    _description = "Todo Stage"

    name = fields.Char("Stage Name", required=True, help="Name")
    sequence = fields.Integer(default=1, string="Sequence",
                              help="Sequence for stages")
    fold = fields.Boolean("Folded By Default", help="Make the stage folded")
    