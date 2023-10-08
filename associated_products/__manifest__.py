# -*- coding: utf-8 -*-
{
    "name": "Associated Products",
    "version": "16.0.1.0.0",
    "category": "Sales",
    "summary": "Adding associated products to customers.",
    "description": """
    This module is used to associate specific products to customers.
    """,
    "author": "Advaith",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["base", "sale"],
    "data": [
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
}
