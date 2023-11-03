# -*- coding: utf-8 -*-
from odoo import fields, models


class ComboProduct(models.Model):
    """
    To add list of combo products
    """
    _name = "combo.product"
    _description = "Combo Product"

    product_tmpl_id = fields.Many2one("product.template",
                                      help="Product id")
    pos_categ_id = fields.Many2one("pos.category",
                                   help="pos category",
                                   required=True)
    product_ids = fields.Many2many("product.product", help="Product",
                                 required=True,
                                 domain="[('product_tmpl_id.pos_categ_id', "
                                        + "'=', pos_categ_id)]")
    is_required = fields.Boolean("Is Required",
                                 help="Is a required combo product")
    quantity = fields.Integer(string="Quantity", help="Quantity",
                              default=1, )
