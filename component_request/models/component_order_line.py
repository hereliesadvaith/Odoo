# -*- coding: utf-8 -*-

from odoo import fields, models


class ComponentOrderLine(models.Model):
    """
    This class is used to make the model of our order line in component
    request page.
    """
    _name = "component.order.line"
    _description = "Component Order Line"

    order_id = fields.Many2one('component.request', string='Order Reference')
    product_id = fields.Many2one("product.product", string="Product")
    quantity = fields.Integer(string="Quantity")
    transfer_type = fields.Selection(string="Transfer Type",
                                     selection=[
                                         ("purchase", "Purchase Order"),
                                         ("internal", "Internal Transfer")
                                     ])
    source_location = fields.Many2one("stock.location")
    destination_location = fields.Many2one("stock.location")
