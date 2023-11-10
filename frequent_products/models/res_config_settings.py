# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    """
    To inherit Configuration page of sale.
    """
    _inherit = 'res.config.settings'

    no_of_months = fields.Integer("No of Months", help="No of Months",
                                  config_parameter="frequent_products.no_of_months")
    select_limit = fields.Integer("Select Limit", help="Select limit",
                                  config_parameter="frequent_products.select_limit")
 