# -*- coding: utf-8 -*-
{
    'name': 'GraphQL Odoo',
    'version': '18.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """GraphQL API for odoo.""",
    'description': """
        GraphQL API for odoo.
     """,
    'author': 'Advaith B G',
    'website': 'https://hereliesadvaith.github.io',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/graphql_schema_views.xml',
    ],
    'license': 'LGPL-3',
    'external_dependencies': {
        'python': [
            'graphene', 'graphql_server'
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
