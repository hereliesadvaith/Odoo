# -*- coding: utf-8 -*-

from odoo import fields, models


class ComponentOrderLine(models.Model):
    """
    This class is used to make the model of our Request For Warranty page
    """
    _name = "component.order.line"
    _description = "Component Order Line"

    order_id = fields.Many2one('component.request', required=True)
    product_id = fields.Many2one("product.product", string="Product")
    quantity = fields.Integer(string="Quantity")
    transfer_type = fields.Selection(string="Transfer Type",
                                     selection=[
                                         ("purchase", "Purchase Order"),
                                         ("internal", "Internal Transfer")
                                     ])
