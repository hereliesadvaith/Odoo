# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductTemplate(models.Model):
    """
    To add fields to product template model.
    """

    _inherit = "product.template"

    manufacture_ok = fields.Boolean(
        string="Can be Manufactured", help="Check product can be manufactured")
    # detailed_type = fields.Selection(selection_add=[
    #     ('raw', 'Raw Material')
    # ], tracking=True, ondelete={'raw': 'set consu'})
    # type = fields.Selection(selection_add=[
    #     ('raw', 'Raw Material')
    # ], ondelete={'raw': 'set consu'})
    component_ids = fields.One2many("required.component", "product_tmpl_id")
