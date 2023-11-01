# -*- coding: utf-8 -*-
{
    "name": "Monthly Sale Report",
    "version": "16.0.1.0.0",
    "category": "Sales",
    "summary": "To generate Monthly and Weekly Reports",
    "description": """
    This module will help you to create shedule actions for automatically generating
    reports and mailing them to sales managers.
    """,
    "author": "Advaith",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["base", "mail", "sale"],
    "data": [
        "security/ir.model.access.csv",
        "data/sale_report_mail_template.xml",
        "data/cron_monthly_sale_report.xml",
        "report/pdf_sale_report_action.xml",
        "report/pdf_sale_report_template.xml",
        "views/sale_report_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
}
