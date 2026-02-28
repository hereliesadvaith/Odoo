# -*- coding: utf-8 -*-
from contextlib import contextmanager
from pathlib import Path
from odoo.api import Environment, SUPERUSER_ID
from odoo.orm.registry import Registry
from odoo.service import server
from odoo.tools import config


BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = BASE_DIR / "odoo.conf"

config.parse_config(["--config", str(CONFIG_PATH)])
server.load_server_wide_modules()
registry = Registry("19C1")


@contextmanager
def get_env(user_id=SUPERUSER_ID):
    with registry.cursor() as cr:
        env = Environment(cr, user_id, {})
        try:
            yield env
            cr.commit()
        except Exception:
            cr.rollback()
            raise
