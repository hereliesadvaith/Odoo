# -*- coding: utf-8 -*-
{
    "name": "QR Code Generator",
    "version": "16.0.1.0.0",
    "category": "Hidden",
    "summary": "To add QR Code Generator.",
    "description": """
    This module is used to create a QR Code generator.
    """,
    "author": "Advaith",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/qr_code_generator_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "qr_code_generator/static/src/js/**/*",
            "qr_code_generator/static/src/xml/qr_code.xml",
        ],
    },
    "license": "LGPL-3",
    "installable": True,
}
