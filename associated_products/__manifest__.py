# -*- coding: utf-8 -*-
{
    "name": "Associated Products",
    "version": "16.0.1.0",
    "category": "Sales",
    "summary": "Adding associated products",
    "description": """
    This module is used to add associated product option in odoo 
    built-in modules.
    """,
    "depends": ["base", "sale", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
    "author": "Advaith",
}
