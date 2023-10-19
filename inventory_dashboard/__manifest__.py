# -*- coding: utf-8 -*-
{
    "name": "Inventory Dashboard",
    "version": "16.0.1.0.0",
    "category": "Inventory",
    "summary": "To add dashboard to inventory",
    "description": """
    This module will add dashboard with features Stock incoming (product wise), 
    Stock outgoing (product wise), Location wise stock info,
    Group based on picking type, Internal transfers (Product wise),
    Warehouse and its location,
    Average expense of  a product(purchase cost + landed cost),
    Inventory valuation, Filter by month,week, User - Only his/her transfers
    and Manager - Complete transfers.
    """,
    "author": "Advaith",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["base", "stock"],
    "data": [
        "views/inventory_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "inventory_dashboard/static/src/dashboard/inventory_dashboard.xml",
            "inventory_dashboard/static/src/dashboard/inventory_dashboard.js",
            "inventory_dashboard/static/src/dashboard/inventory_card.xml",
            "inventory_dashboard/static/src/dashboard/inventory_card.js",
        ],
    },
    "license": "LGPL-3",
    "installable": True,
}
