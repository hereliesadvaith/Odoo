# -*- coding: utf-8 -*-

from odoo import api, models


class Picking(models.Model):
    """
    To inherit validation button.
    """
    _inherit = "stock.picking"
    def button_validate(self):
        """
        To validate transfer and change state of our request for warranty.
        """
        super(Picking, self).button_validate()
        warranties = self.env["request.for.warranty"].search([
            ("name", '=', self.origin)
        ])
        picking_type_in = self.env.ref("stock.picking_type_in").id
        for warranty in warranties:
            if self.picking_type_id.id == picking_type_in:
                warranty.state = 'received'
            else:
                warranty.state = 'done'
