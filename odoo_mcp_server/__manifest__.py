# -*- coding: utf-8 -*-
{
    "name": "Odoo MCP Server",
    "version": "19.0.1.0.0",
    "category": "Tools",
    "summary": "MCP server for odoo.",
    "description": "MCP server for odoo.",
    "author": "Advaith B G",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["base", "mail", "contacts", "im_livechat"],
    "external_dependencies": {
        "python": ["google-generativeai"]
    },
    "data": [
        "data/ir_action_server.xml",
        "security/ir.model.access.csv",
        "views/chatbot_script_views.xml"
    ],
    "license": "LGPL-3",
    "installable": True,
}
