# -*- coding: utf-8 -*-
from odoo import fields, models


class Slide(models.Model):
    """
    To inherit course content model
    """
    _inherit = "survey.survey"

    idle_time = fields.Integer("Idle Time Start Delay (s)",
                             help="Set starting delay time")
    turn_page_time = fields.Integer("Page Turn Delay (s)",
                                  help="Set page turn delay time")
