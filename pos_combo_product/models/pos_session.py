# -*- coding: utf-8 -*-
from odoo import models


class PosSession(models.Model):
    """
    To inherit pos session model.
    """
    _inherit = "pos.session"

    def _loader_params_product_product(self):
        """
        To add product owner id in parameters
        """
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('is_combo')
        return result
