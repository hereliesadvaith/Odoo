# -*- coding: utf-8 -*-
{
    "name": "Payment Provider: PayU Payment Services",
    "version": "16.0.1.0.0",
    "category": "Accounting/Payment Providers",
    "summary": "PayU payment provider covering India.",
    "description": """
    This module is used to integrate PayU payment provider with our
    odoo.
    """,
    "author": "Advaith",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["payment"],
    "data": [
        'views/payment_provider_views.xml',
        'views/payment_payu_templates.xml',
        'data/payment_provider_data.xml',
    ],
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
    "license": "LGPL-3",
}
