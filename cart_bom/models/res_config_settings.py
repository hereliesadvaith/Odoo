# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    """
    To inherit Configuration page of website.
    """
    _inherit = 'res.config.settings'

    show_bom_products = fields.Boolean(
        "Select Multiple Products", store=True)
    bom_product_ids = fields.Many2many(
        'product.product',
        related='website_id.bom_product_ids',
        readonly=False,
    )

    def set_values(self):
        """
        To set the field value.
        """
        result = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'show_bom_products',
            self.show_bom_products)
        self.website_id.update({
            'bom_product_ids': [(fields.Command.link(
                i)) for i in self.bom_product_ids.ids
            ]
        })
        return result

    @api.model
    def get_values(self):
        """
        To get the field value.
        """
        result = super(ResConfigSettings, self).get_values()
        result['show_bom_products'] = self.env[
            'ir.config_parameter'].sudo().get_param(
            'show_bom_products'
        )
        return result


class Website(models.Model):
    """
    To add a field in website model to save the values.
    """
    _inherit = 'website'

    bom_product_ids = fields.Many2many('product.product')
