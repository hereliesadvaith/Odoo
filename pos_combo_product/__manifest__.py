# -*- coding: utf-8 -*-
{
    "name": "POS Combo Product",
    "version": "16.0.1.0",
    "author": "Advaith",
    "category": "Sales",
    "summary": "Can sell combo products inside POS.",
    "description": """
    This module helps to create combo products inside product template page
    and sell those product on POS.
    """,
    "depends": ["base", "point_of_sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_views.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_combo_product/static/src/js/*",
            "pos_combo_product/static/src/xml/*",
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}