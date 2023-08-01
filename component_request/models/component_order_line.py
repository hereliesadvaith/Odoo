# -*- coding: utf-8 -*-
from odoo import fields, models


class ComponentOrderLine(models.Model):
    """
    This class is used to make the model of our order line in component
    request page.
    """
    _name = "component.order.line"
    _description = "Component Order Line"

    order_id = fields.Many2one('component.request', string='Order Reference',
                               help="Order")
    product_id = fields.Many2one(
        "product.product", string="Product", help="Product")
    quantity = fields.Integer(string="Quantity", help="Quantity")
    transfer_type = fields.Selection(string="Transfer Type",
                                     selection=[
                                         ("purchase", "Purchase Order"),
                                         ("internal", "Internal Transfer")
                                     ],
                                     required=True, help="Transfer type")
    source_location = fields.Many2one(
        "stock.location", help="Source location of product")
    destination_location = fields.Many2one(
        "stock.location", help="Destination location of product")
