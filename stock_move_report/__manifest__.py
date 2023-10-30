# -*- coding: utf-8 -*-
{
    "name": "Stock Move Report",
    "version": "16.0.1.0.0",
    "category": "Inventory",
    "summary": "To add stock moves report feature.",
    "description": """
    This module will add a wizard for creating report of stock moves of current company.
    """,
    "author": "Advaith",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["base", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/inventory_report_wizard_views.xml",
        "report/inventory_template.xml",
        "report/inventory_report.xml",
        "views/inventory_menus.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
}
