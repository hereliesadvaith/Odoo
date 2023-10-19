# -*- coding: utf-8 -*-
from odoo.http import request
from odoo.addons.survey.controllers.main import Survey


class Survey(Survey):
    """
    To inherit survey controller
    """

    def survey_submit(self, survey_token, answer_token, **post):
        """
        To extend survey_display_page function.
        """
        result = super(Survey, self).survey_submit(
            survey_token, answer_token, **post
        )
        access_data = self._get_access_data(survey_token, answer_token,
                                            ensure_token=True)
        survey_user_input_id = access_data["answer_sudo"]
        vals = {}
        if survey_user_input_id.state == "done":
            for input_line in survey_user_input_id.user_input_line_ids.filtered(
                lambda r: r.question_id.id in survey_user_input_id.survey_id.
                        survey_contact_ids.question_id.ids
            ):
                contact = survey_user_input_id.survey_id.survey_contact_ids.filtered(
                    lambda r: r.question_id == input_line.question_id
                )
                vals[contact.partner_fields_id.name] = input_line.display_name
            request.env["res.partner"].sudo().create(vals)
        return result
