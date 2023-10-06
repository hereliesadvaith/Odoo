# -*- coding: utf-8 -*-
{
    "name": "Merge Invoice Lines",
    "version": "16.0.1.0",
    "author": "Advaith",
    "category": "Sales",
    "summary": "Invoice line merging for multiple sale orders.",
    "description": """
    When creating invoice with merged sale orders this module helps to show 
    sale order details on invoice line.
    """,
    "depends": ["base", "sale", "stock"],
    "data": [
        "views/account_move_line_views.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
