# -*- coding: utf-8 -*-
from odoo import models


class ProductProduct(models.Model):
    """
    To add purchase button action in product variants page
    """
    _inherit = "product.product"

    # Action Methods

    def action_automate_po(self):
        """
        To open the wizard on button click.
        """
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'auto.purchase',
            'name': 'Auto Purchase',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_product_id': self.id,
                'default_price':
                    self.seller_ids[0].price if self.seller_ids else False,
                'default_vendor':
                    self.seller_ids[0].partner_id.id if self.seller_ids
                    else False,
            }
        }
