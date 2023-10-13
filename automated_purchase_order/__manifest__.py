# -*- coding: utf-8 -*-
{
    "name": "Automated Purchase Order",
    "version": "16.0.1.0.0",
    "category": "Sales",
    "summary": "Create purchase order from product form view.",
    "description": """
    This module lets you create purchase order from product view 
    with one button click.
    """,
    "author": "Advaith",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["base", "purchase", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_product_views.xml",
        "wizard/auto_purchase_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
}
