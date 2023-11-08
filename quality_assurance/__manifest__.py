# -*- coding: utf-8 -*-
{
    "name": "Quality Assurance",
    "version": "16.0.1.0",
    "author": "Advaith",
    "category": "Inventory",
    "summary": "To manage basic quality assurance procedure",
    "description": """
    This module provides features to manage basic quality assurance procedure.
    """,
    "depends": ["base", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "data/quality_alert_sequence.xml",
        "views/quality_measure_views.xml",
        "views/quality_alert_views.xml",
        "views/quality_test_views.xml",
        "views/quality_assurance_menus.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
