# -*- coding: utf-8 -*-
{
    "name": "Frequent Products",
    "version": "16.0.1.0.0",
    "category": "Sales",
    "summary": "Adding frequent products to customers.",
    "description": """
    This module is used to show recently bought products inside customers page.
    """,
    "author": "Advaith",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["base", "sale"],
    "data": [
        "views/res_config_settings_views.xml",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
}
