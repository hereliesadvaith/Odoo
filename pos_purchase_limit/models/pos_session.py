# -*- coding: utf-8 -*-
from odoo import models


class PosSession(models.Model):
    """
    To inherit pos session model.
    """
    _inherit = "pos.session"

    def _loader_params_res_partner(self):
        """
        To add product owner id in parameters
        """
        result = super()._loader_params_res_partner()
        result['search_params']['fields'].extend(['enable_purchase_limit'])
        result['search_params']['fields'].extend(['purchase_limit_value'])
        result['search_params']['fields'].extend(['total_session_amount'])
        return result
