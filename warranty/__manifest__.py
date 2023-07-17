# -*- coding: utf-8 -*-

{
    "name": "Warranty",
    "version": "16.0.1.0",
    "category": "Services",
    "summary": "Requesting Warranty",
    "depends": ["base", "account", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "security/warranty_security.xml",
        "data/warranty_sequence.xml",
        "views/request_for_warranty_views.xml",
        "views/product_template_views.xml",
        "views/warranty_menus.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
    "author": "Advaith B G",
}
