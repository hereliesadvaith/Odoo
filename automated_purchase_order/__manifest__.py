# -*- coding: utf-8 -*-

{
    "name": "Automated Purchase Order",
    "version": "16.0.1.0",
    "category": "Sales",
    "summary": "Create purchase order from product view.",
    "description": """
    This module lets you create purchase order from product view 
    with one button click.
    """,
    "depends": ["base", "sale", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_views.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
    "author": "Advaith",
}