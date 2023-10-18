# -*- coding: utf-8 -*-
from odoo import fields, models


class Survey(models.Model):
    """
    To inherit survey model.
    """
    _inherit = "survey.survey"

    survey_contact_ids = fields.One2many("survey.contact",
                                         "survey_id",
                                         help="Contact Creation Page")
