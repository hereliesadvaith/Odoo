# -*- coding: utf-8 -*-
{
    "name": "Order History",
    "version": "16.0.1.0",
    "author": "Advaith",
    "category": "Sales",
    "summary": "History of sale orders and corresponding purchase orders.",
    "description": """
    This module helps you view history of sale orders and corresponding 
    purchase orders. Also this module have many sale moudle extension features.
    """,
    "depends": ["base", "sale", "purchase"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/product_product_views.xml",
        "views/order_history_views.xml",
        "data/cron_order_history.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
