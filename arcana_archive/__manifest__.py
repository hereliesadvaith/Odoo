# -*- coding: utf-8 -*-
{
    'name': 'Arcana Archive',
    'version': '18.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Backend functions for Arcana Archive.""",
    'description': """
        Backend functions for Arcana Archive.
     """,
    'author': 'Advaith B G',
    'website': 'https://hereliesadvaith.github.io',
    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': [
            'arcana_archive/static/src/scss/theme.scss',
        ]
    },
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
