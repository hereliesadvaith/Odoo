# -*- coding: utf-8 -*-
{
    "name": "Simple Production",
    "version": "16.0.1.0",
    "author": "Advaith",
    "category": "Manufacturing",
    "summary": "Manufacturing Orders",
    "description": """
    This module is used to make manufacturing orders.
    """,
    "depends": ["base", "product", "purchase", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "data/simple_production_sequence.xml",
        "data/production_location.xml",
        "views/product_template_views.xml",
        "views/simple_production_views.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
