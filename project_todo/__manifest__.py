# -*- coding: utf-8 -*-
{
    "name": "To-Do",
    "version": "16.0.1.0.0",
    "category": "Productivity",
    "summary": "Organize your work to-do lists",
    "description": """
    This module helps you organize your work with to-do lists.
    """,
    "author": "Advaith",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["base", "project"],
    "data": [
        "security/ir.model.access.csv",
        "views/todo_task_views.xml",
        "views/project_todo_menus.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
}
