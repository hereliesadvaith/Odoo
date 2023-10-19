# -*- coding: utf-8 -*-
from odoo import models


class ProductProduct(models.Model):
    """
    To add purchase button action in product variants page
    """
    _inherit = "product.product"

    def get_stocks(self):
        """
        To return stock data.
        """
        product_count = {
            "new_count": 10
        }
        return product_count
