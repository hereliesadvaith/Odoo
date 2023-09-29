# -*- coding: utf-8 -*-
{
    "name": "Bill of Materials in Cart",
    "version": "16.0.1.0",
    "author": "Advaith",
    "category": "Website",
    "summary": "Bill of materails of product in cart page.",
    "description": """
    This module will show the bill of materials of the 
    products after the product description.
    """,
    "depends": ["base", "sale", "website", "mrp"],
    "data": [
        "views/res_config_settings_views.xml",
        "views/cart_template_views.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
