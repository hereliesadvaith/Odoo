# -*- coding: utf-8 -*-
import hashlib
import logging

from odoo import fields, models


_logger = logging.getLogger(__name__)


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('payu', "PayU Payment Services")], ondelete={'payu': 'set default'}
    )
    payu_key = fields.Char("PayU Key", help="Secret Key")
    payu_salt = fields.Char("PayU Salt", help="Salt for encryption")
