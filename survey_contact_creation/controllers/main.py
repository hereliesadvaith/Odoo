# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.survey.controllers.main import Survey


class Survey(Survey):
    """
    To inherit survey controller
    """

    @http.route('/survey/submit/<string:survey_token>/<string:answer_token>',
                type='json', auth='public', website=True)
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
        if survey_user_input_id.state == "done":
            print("hello")
        return result
