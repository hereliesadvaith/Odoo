# -*- coding: utf-8 -*-
{
    "name": "POS Purchase Limit",
    "version": "16.0.1.0",
    "author": "Advaith",
    "category": "Sales",
    "summary": "Can add purchase limit to customers.",
    "description": """
    This module helps to set limit for customer
    purchases in POS.
    """,
    "depends": ["base", "sale", "point_of_sale"],
    "data": [
        "views/res_partner_views.xml",
    ],
    "assets": {
        'point_of_sale.assets': [
            'pos_purchase_limit/static/src/js/**/*',
            'pos_purchase_limit/static/src/xml/pos_screen.xml',
       ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
