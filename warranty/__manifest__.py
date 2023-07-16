# -*- coding: utf-8 -*-

{
    "name": "Warranty",
    "version": "16.0.1.0",
    "summary": "Requesting Warranty",
    "depends": ["base", "account", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "data/warranty_sequence.xml",
        "views/request_for_warranty_views.xml",
        "views/warranty_type_views.xml",
        "views/warranty_menu_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
    "author": "Advaith B G",
}
