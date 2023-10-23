# -*- coding: utf-8 -*-
from odoo import models


class InventoryDashboard(models.AbstractModel):
    """
    To get values for inventory dashboard.
    """

    _name = "inventory.dashboard"
    _description = "Inventory Dashboard"

    def get_stock_incoming(self, domain):
        """
        To get incoming stocks
        """
        print(domain)
        products = self.env["product.product"].sudo().search(domain).filtered(
            lambda r: r.incoming_qty > 0)
        print(products)
        return {
            "products": [i.name for i in products],
            "incoming_qty": [i.incoming_qty for i in products]
        }

    def get_stock_outgoing(self, domain):
        """
        To get outgoing stocks
        """
        print(domain)
        products = self.env["product.product"].sudo().search(domain).filtered(
            lambda r: r.outgoing_qty > 0)
        print(products)
        return {
            "products": [i.name for i in products],
            "outgoing_qty": [i.outgoing_qty for i in products]
        }
