# -*- coding: utf-8 -*-
from odoo import models, fields


class PosConfig(models.Model):
    """
    To inherit Configuration page of POS.
    """
    _inherit = 'pos.config'

    set_due_limit = fields.Boolean("Due Limit",
                                   help="enable to set limit")
    due_limit_value = fields.Float("Limit",
                                   help="to add limit")


class ResConfigSettings(models.TransientModel):
    """
    To inherit settings page
    """
    _inherit = "res.config.settings"

    pos_set_due_limit = fields.Boolean(
        related='pos_config_id.set_due_limit', readonly=False)
    pos_due_limit_value = fields.Float(
        related='pos_config_id.due_limit_value', readonly=False)

class ResPartner(models.Model):
    """
    To add fields in contact creation page.
    """
    _inherit = "res.partner"

    balance_due = fields.Float("Balance Due", help="Balance due")
