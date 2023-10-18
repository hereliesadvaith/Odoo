# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class PaymentProvider(models.Model):
    """
    To add fields in Payment Provider model.
    """
    _inherit = 'payment.provider'

    maximum_amount = fields.Monetary(
        string="Maximum Amount",
        help="The maximum payment amount that this payment provider is "
             "available for.",
        currency_field='main_currency_id',
    )
    minimum_amount = fields.Monetary(
        string="Minimum Amount",
        help="The minimum payment amount that this payment provider is "
             "available for.",
        currency_field='main_currency_id',
    )

    # Constrains Methods

    @api.constrains("maximum_amount", "minimum_amount")
    def _constrains_amounts(self):
        """
        Validation of minimum and max amounts.
        """
        if self.minimum_amount > self.maximum_amount:
            raise ValidationError(
                "Minimum amount should be lower than maximum amount"
            )

    # Business Methods

    @api.model
    def _get_compatible_providers(
            self, company_id, partner_id, amount, currency_id=None,
            force_tokenization=False,
            is_express_checkout=False, is_validation=False, **kwargs
    ):
        """
        To add our conditions in _get_compatible_providers
        """
        result = super(PaymentProvider, self)._get_compatible_providers(
            company_id, partner_id, amount, currency_id=None,
            force_tokenization=False,
            is_express_checkout=False, is_validation=False, **kwargs
        )
        currency = self.env['res.currency'].browse(currency_id).exists()
        company = self.env['res.company'].browse(company_id).exists()
        date = fields.Date.context_today(self)
        converted_amount = currency._convert(amount, company.currency_id,
                                             company, date)
        result = result.filtered(lambda r:
                                 (r.maximum_amount >= converted_amount or
                                  r.maximum_amount == 0) and
                                 (r.minimum_amount <= converted_amount or
                                  r.minimum_amount == 0)
                                 )
        return result
