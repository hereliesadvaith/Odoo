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
        result['search_params']['fields'].append('combo_product_ids')
        return result
    
    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        result.append('combo.product')
        return result
    
    def _loader_params_combo_product(self):
    
        return { 
            'search_params': {  
                'domain': [],  
                'fields': ['pos_categ_id', 'product_ids', 'is_required', 'quantity'],
            },
        }
    
    def _get_pos_ui_combo_product(self, params):
        return self.env['combo.product'].search_read(
            **params['search_params'])
