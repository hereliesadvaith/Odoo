# -*- coding: utf-8 -*-
from odoo import fields, models


class PaymentProvider(models.Model):
    """
    To add fields in Payment Provider model.
    """
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('payu', "PayU Payment Services")], ondelete={'payu': 'set default'}
    )
    payu_key = fields.Char("PayU Key", help="Secret Key")
    payu_salt = fields.Char("PayU Salt", help="Salt for encryption")
