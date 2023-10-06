# -*- coding: utf-8 -*-
from odoo import models, api


class AccountMove(models.Model):
    """
    To inherit create invoice button
    """
    _inherit = 'account.move'

    @api.onchange('payment_reference')
    def onchange_payment_reference(self):
        """
        Merge order lines
        """
        print(self.line_ids.sale_line_ids.order_id)
