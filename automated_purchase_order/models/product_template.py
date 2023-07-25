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
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'auto.purchase',
            'name': 'Auto Purchase',
            'view_mode': 'form',
            'target': 'new',
        }
