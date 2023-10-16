# -*- coding: utf-8 -*-
{
    "name": "Project Template",
    "version": "16.0.1.0.0",
    "category": "Services",
    "summary": "Adding templates for Projects and Tasks",
    "description": """
    This module is used to create template model for Projects
    and Tasks.
    """,
    "author": "Advaith",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["base", "project"],
    "data": [
        "security/ir.model.access.csv",
        "views/project_template_views.xml",
        "views/task_template_views.xml",
        "views/project_menu_items.xml",
        "views/project_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
}
