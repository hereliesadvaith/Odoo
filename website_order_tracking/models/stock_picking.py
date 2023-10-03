# -*- coding: utf-8 -*-
from odoo import models, fields, api


class StockPicking(models.Model):
    """
    To inherit transfer model.
    """
    _inherit = "stock.picking"

    track_order_ids = fields.One2many('track.order',
                                      "transfer_id")
