# -*- coding: utf-8 -*-

from odoo import models


class ProductsTemplate(models.Model):
    """
    To add fields to product template model.
    """

    _inherit = "product.template"

    # Action Methods

    def action_automate_po(self):
        """
        To open the wizard.
        """
        product_id = self.env["product.product"].search([
            ("product_tmpl_id", "=", self.id)
        ])
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'auto.purchase',
            'name': 'Auto Purchase',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_product_id': product_id.id,
                'default_price':
                    (self.seller_ids)[0].price if self.seller_ids else False,
                'default_vendor':
                    (self.seller_ids)[0].partner_id.id if self.seller_ids
                    else False,
            }
        }
