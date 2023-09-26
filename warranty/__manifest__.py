# -*- coding: utf-8 -*-
{
    "name": "Warranty",
    "version": "16.0.1.0",
    "author": "Advaith",
    "category": "Services",
    "summary": "Requesting Warranty",
    "description": """
    This module is used to send requests to vendors for the warranty.
    """,
    "depends": ["base", "account", "stock", "website", "portal"],
    "data": [
        "security/ir.model.access.csv",
        "security/warranty_security.xml",
        "data/warranty_sequence.xml",
        "data/warranty_location.xml",
        "report/warranty_report.xml",
        "report/warranty_template.xml",
        "wizard/warranty_report_views.xml",
        "views/request_for_warranty_views.xml",
        "views/product_template_views.xml",
        "views/account_move_views.xml",
        "views/warranty_menus.xml",
        "views/warranty_website_view.xml",
        "views/warranty_snippet_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "warranty/static/src/js/action_manager.js",
        ],
        "web.assets_frontend": [
            "warranty/static/src/js/warranty_request.js",
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
