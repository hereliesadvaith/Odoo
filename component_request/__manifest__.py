# -*- coding: utf-8 -*-
{
    "name": "Component Request",
    "version": "16.0.1.0",
    "category": "Sales",
    "summary": "Employees can create components requests.",
    "description": """
    This module let's employees to create components requests and
    submit to requistion managers.
    """,
    "depends": ["base", "purchase", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "security/component_request_security.xml",
        "views/component_request_views.xml",
        "views/component_order_line_views.xml",
        "data/component_request_sequence.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
    "author": "Advaith",
}
