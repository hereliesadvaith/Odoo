# -*- coding: utf-8 -*-
{
    "name": "Supplier Info",
    "version": "16.0.1.0",
    "author": "Advaith",
    "category": "Sales",
    "summary": "Supplier info",
    "description": """
    You can compare purchase orders.
    """,
    "depends": ["base", "purchase"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/compare_price_views.xml",
        "views/purchase_order_views.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
