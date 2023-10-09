# -*- coding: utf-8 -*-
import logging
from odoo import models

_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    """
    To inherit payment transaction model.
    """
    _inherit = "payment.transaction"

    def _get_specific_rendering_values(self, processing_values):
        """
        To add values to processing values
        """
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'payu':
            return res
        salt = self.provider_id.payu_salt
        txnid = "a1svtbbjRd24wa"
        rendering_values = {
            "key": self.provider_id.payu_key,
            "txnid": txnid,
        }
        return rendering_values

        # hash = sha512(key | txnid | amount | productinfo | firstname | email | SALT)
