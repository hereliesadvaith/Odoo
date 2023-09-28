# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    """
    To inherit Configuration page of website.
    """
    _inherit = 'res.config.settings'

    enable_select_multiple_products = fields.Boolean(
        "Select Multiple Products", store=True)

    def set_values(self):
        """
        To set the field value.
        """
        result = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'enable_select_multiple_products',
            self.enable_select_multiple_products)
        return result

    @api.model
    def get_values(self):
        """
        To get the field value.
        """
        result = super(ResConfigSettings, self).get_values()
        result['enable_select_multiple_products'] = self.env[
            'ir.config_parameter'].sudo().get_param(
            'enable_select_multiple_products'
        )
        return result
