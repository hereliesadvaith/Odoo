# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductsTemplate(models.Model):
    """
    To add fields to product template model.
    """

    _inherit = "product.template"

    # Action Methods

    def action_automate_po(self):
        pass
