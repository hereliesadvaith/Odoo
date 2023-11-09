# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    """
    To inherit Configuration page of sale.
    """
    _inherit = 'res.config.settings'

    no_of_months = fields.Integer("No of Months")
    select_limit = fields.Integer("Select Limit")

    def set_values(self):
        """
        To set the field value.
        """
        result = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'no_of_months',
            self.no_of_months)
        self.env['ir.config_parameter'].sudo().set_param(
            'select_limit',
            self.select_limit)
        return result

    @api.model
    def get_values(self):
        """
        To get the field value.
        """
        result = super(ResConfigSettings, self).get_values()
        result['no_of_months'] = self.env[
            'ir.config_parameter'].sudo().get_param(
            'no_of_months'
        )
        result['select_limit'] = self.env[
            'ir.config_parameter'].sudo().get_param(
            'select_limit'
        )
        return result
    