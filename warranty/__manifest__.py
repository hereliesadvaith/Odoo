# -*- coding: utf-8 -*-

{
    "name": "Warranty",
    "version": "16.0.1.0",
    "category": "Services",
    "summary": "Requesting Warranty",
    "description": """
    This module is used to send requests to vendors for the warranty.
    """,
    "depends": ["base", "account", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "security/warranty_security.xml",
        "data/warranty_sequence.xml",
        "data/warranty_location.xml",
        "views/request_for_warranty_views.xml",
        "views/product_template_views.xml",
        "views/account_move_views.xml",
        "views/warranty_menus.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
    "author": "Advaith",
}
