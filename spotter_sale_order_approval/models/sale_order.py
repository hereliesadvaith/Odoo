# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrder(models.Model):
    """
    To add fields in invoice page.
    """
    _inherit = "sale.order"

    is_above_limit = fields.Boolean("is_above_limit", default=False)
    is_approved = fields.Boolean("is_approved", default=False)

    # Compute Methods

    @api.onchange("order_line")
    def _onchange_order_line(self):
        """
        To show approve button
        """
        if self.state == "draft":
            if self.amount_total >= 25000:
                self.is_above_limit = True
            else:
                self.is_above_limit = False

    # Action Methods

    def action_approve(self):
        """
        To approve sale order
        """
        self.is_above_limit = False
