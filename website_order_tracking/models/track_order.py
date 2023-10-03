# -*- coding: utf-8 -*-
from odoo import models, fields, api


class TrackOrder(models.Model):
    """
    To inherit transfer model.
    """
    _name = 'track.order'
    _description = 'Track Order'

    transfer_id = fields.Many2one('stock.picking',
                                  help="Transfer id")
    from_address = fields.Text("From")
    to_address = fields.Text("To")
    deadline = fields.Date(default=fields.Date.today())
    state = fields.Selection(
        selection=[
            ("ongoing", "Ongoing"),
            ("completed", "Completed"),
        ],
        default="ongoing",
        help="Status of the transfers"
    )

    # Action Methods

    def action_change_state(self):
        """
        To change state of transfer
        """
        self.ensure_one()
        if self.state == "ongoing":
            self.state = "completed"
