# -*- coding: utf-8 -*-
{
    "name": "Restrict Payment Acquirer",
    "version": "16.0.1.0.0",
    "category": "Sales",
    "summary": "Restrict payment acquirers based on the order amount",
    "description": """
    Restrict payment acquirers based on the order amount. 
    Users are able to set a minimum and maximum amount on which each payment acquirer applies.
    """,
    "author": "Advaith",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["base", "payment"],
    "data": [
        "views/payment_provider_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
}
