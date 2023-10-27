# -*- coding: utf-8 -*-
{
    "name": "POS Product Creation",
    "version": "16.0.1.0",
    "author": "Advaith",
    "category": "Sales",
    "summary": "Can create and edit products from POS.",
    "description": """
    This module helps to create and edit products from POS.
    """,
    "depends": ["base", "point_of_sale"],
    "assets": {
        "point_of_sale.assets": [
            "pos_product_creation/static/src/js/*",
            "pos_product_creation/static/src/xml/*",
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
