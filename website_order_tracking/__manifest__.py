# -*- coding: utf-8 -*-
{
    "name": "Website Order Tracking",
    "version": "16.0.1.0",
    "author": "Advaith",
    "category": "Website",
    "summary": "Tracking of orders in website.",
    "description": """
    This module will help to show the details of the delivery of sales
    orders.
    """,
    "depends": ["base", "sale", "website", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/website_portal_views.xml",
        "views/stock_picking_views.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
