# -*- coding: utf-8 -*-

{
    "name": "Simple Production",
    "version": "16.0.1.0",
    "category": "Manufacturing",
    "summary": "Manufacturing Orders",
    "description": """
    This module is used to make manufacturing orders.
    """,
    "depends": ["base", "product", "purchase", "stock"],
    "data": [
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "license": "LGPL-3",
    "author": "Advaith",
}
