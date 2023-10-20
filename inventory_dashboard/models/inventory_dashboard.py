# -*- coding: utf-8 -*-
from odoo import models


class InventoryDashboard(models.Model):
    """
    To get values for inventory dashboard
    """
    _name = "inventory.dashboard"
    _description = "Inventory Dashboard"

    def get_product_details(self):
        """
        To get product details
        """
        result = []
        products = self.env["product.product"].browse(12)
        for product in products:
            product_details = {'product': product.name}
            result.append(product_details)
        print(result)
        result = {
            "count": 10,
        }
        return result
