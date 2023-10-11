# -*- coding: utf-8 -*-
from odoo import fields, models


class Slide(models.Model):
    """
    To inherit course content model
    """
    _inherit = "survey.survey"

    idle_time = fields.Float("Idle Time Start Delay",
                             help="Set starting delay time")
    turn_page_time = fields.Float("Page Turn Delay",
                                  help="Set page turn delay time")
