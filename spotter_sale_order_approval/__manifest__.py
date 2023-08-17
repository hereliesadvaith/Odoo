# -*- coding: utf-8 -*-
{
    "name": "Spotter Sale Order Approval",
    "version": "16.0.1.0",
    "author": "Advaith",
    "category": "Sales",
    "summary": "Sale order approval",
    "description": """
    If the sale order is above a certain limit an approval system is added for 
    that order.
    """,
    "depends": ["base", "sale"],
    "data": [
        "views/sale_order_views.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
