# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrder(models.Model):
    """
    To inherit sale order
    """
    _inherit = "sale.order"

    is_above_limit = fields.Boolean(
        "is_above_limit", compute="_compute_is_above_limit",
        help="Check amount limit")
    is_level_1_approved = fields.Boolean("is_approved", default=False,
                                         help="Check level 1 approval")
    is_level_2_approved = fields.Boolean("is_approved", default=False,
                                         help="Check level 2 approval")

    # Compute Functions

    @api.depends("order_line")
    def _compute_is_above_limit(self):
        """
        To configure boolean fields
        """
        for order in self:
            if (order.amount_total < 25000 or
                    order.state != "draft" or
                    (order.is_level_1_approved and order.is_level_2_approved)):
                order.is_above_limit = False
            else:
                order.is_above_limit = True

    # Action Methods

    def action_approve(self):
        """
        To approve quotation
        """
        self.ensure_one()
        if self.is_level_1_approved:
            self.is_above_limit = False
            self.is_level_2_approved = True
        else:
            self.is_level_1_approved = True
