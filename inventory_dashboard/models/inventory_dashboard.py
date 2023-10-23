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
        domain = [tuple(i) for i in domain]
        print(domain)
        return {
            "stock": 10,
        }
