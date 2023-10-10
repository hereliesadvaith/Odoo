# -*- coding: utf-8 -*-
from werkzeug import urls
from hashlib import sha512
from odoo import api, fields, models
from ..controllers.main import PayUController


class PaymentTransaction(models.Model):
    """
    To inherit payment transaction model.
    """
    _inherit = "payment.transaction"
    transaction_id = fields.Char("Transaction ID", help="Transaction ID")

    # Business Methods

    def _get_specific_rendering_values(self, processing_values):
        """
        To add values to redirect payment form.
        """
        payu_key = self.provider_id.payu_key
        txnid = self.transaction_id
        amount = str(self.amount)
        productinfo = self.reference
        firstname = self.partner_id.name
        email = self.partner_id.email
        phone = self.partner_id.phone
        payu_salt = self.provider_id.payu_salt
        udf1 = udf2 = udf3 = udf4 = udf5 = ""
        concatenated_string = (f"{payu_key}|{txnid}|{amount}|{productinfo}|"
                               f"{firstname}|{email}|{udf1}|{udf2}|{udf3}|"
                               f"{udf4}|{udf5}||||||{payu_salt}")
        base_url = self.provider_id.get_base_url()
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'payu':
            return res
        rendering_values = {
            "key": payu_key,
            "txnid": txnid,
            "amount": amount,
            "productinfo": productinfo,
            "firstname": firstname,
            "email": email,
            "phone": phone,
            "hash": sha512(concatenated_string.encode()).hexdigest(),
            "return_url": urls.url_join(base_url, PayUController._return_url)
        }
        return rendering_values

    # CRUD Methods

    @api.model_create_multi
    def create(self, vals_list):
        """
        Used to create sequence number for our transaction.
        """
        for vals in vals_list:
            if vals['provider_id'] == self.env['payment.provider'].search(
                    [('code', '=', 'payu')]).id:
                vals["transaction_id"] = self.env["ir.sequence"].next_by_code(
                    "payment.transaction"
                )
        result = super(PaymentTransaction, self).create(vals_list)
        return result
