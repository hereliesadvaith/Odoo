# -*- coding: utf-8 -*-
{
    "name": "Sales Dashboard",
    "version": "16.0.1.0.0",
    "category": "Sales",
    "summary": "To add dashboard to sales module.",
    "description": """
    This module will add a dashboard to sales module.
    """,
    "author": "Advaith",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["base", "web", "sale", "board"],
    "data": [
        "views/sales_menu_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "sales_dashboard/static/src/components/sales_dashboard.xml",
            "sales_dashboard/static/src/components/sales_dashboard.js",
            "sales_dashboard/static/src/components/kpi_card/kpi_card.xml",
            "sales_dashboard/static/src/components/kpi_card/kpi_card.js",
        ],
    },
    "license": "LGPL-3",
    "installable": True,
}
