# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class RequestForWarranty(models.Model):
    """
    This class is used to make the model of our Request For Warranty page
    """

    _name = "request.for.warranty"
    _description = "Request For Warranty"

    name = fields.Char(
        required=True, readonly=True, index=True, default=lambda self: _("New")
    )

    @api.model
    def create(self, vals):
        """
        Used to create sequence number for our request for warranty.
        """
        if vals.get("name", _("New")) == _("New"):
            vals["name"] = self.env["ir.sequence"].next_by_code(
                "warranty.sequence"
            ) or _("New")
            result = super(RequestForWarranty, self).create(vals)
            return result

    warranty_type_id = fields.Many2one("warranty.type")
