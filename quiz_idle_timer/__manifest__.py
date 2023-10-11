# -*- coding: utf-8 -*-
{
    "name": "Quiz Idle Timer",
    "version": "16.0.1.0.0",
    "category": "Accounting/Payment Providers",
    "summary": "Timer for quiz pages.",
    "description": """
    This module is used to add a timer in quiz pages.
    """,
    "author": "Advaith",
    "website": "https://hereliesadvaith.github.io",
    "depends": ["website", "survey"],
    "data": [
        "views/survey_survey_views.xml",
        "views/survey_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "quiz_idle_timer/static/src/js/quiz_timer.js",
        ],
    },
    "license": "LGPL-3",
}
