# -*- coding: utf-8 -*-
{
    'name': 'Arcana Backend Theme',
    'version': '20.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Light navbar and accent colours for the Odoo backend.""",
    'description': """
        Restyles the backend navbar with a white background, muted text and a
        blue link accent. Ported from arcana_archive (18.0).
     """,
    'author': 'Advaith B G',
    'website': 'https://hereliesadvaith.github.io',
    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': [
            'backend_theme_arcana/static/src/scss/theme.scss',
        ]
    },
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
