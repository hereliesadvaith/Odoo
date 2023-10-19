# -*- coding: utf-8 -*-
from odoo import fields, models


class SurveyContact(models.Model):
    """
    To add questions and fields
    """
    _name = "survey.contact"
    _description = "Survey Contact"

    survey_id = fields.Many2one("survey.survey",
                                string="Survey ID")
    question_id = fields.Many2one("survey.question",
                                   string="Questions", help="Questions",
                                   domain="[('survey_id', '=', survey_id)]",)
    partner_fields_id = fields.Many2one("ir.model.fields",
                                        help="Partner Fields",
                                        domain=lambda self: [(
                                            'model_id', '=', self.env.ref(
                                                'base.model_res_partner').id)]
                                        )
