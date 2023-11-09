# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    """
    To inherit sales order page.
    """
    _inherit = "sale.order"
