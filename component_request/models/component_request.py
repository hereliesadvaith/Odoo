# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ComponentRequest(models.Model):
    """
    This class is used to make the model of our Request For Warranty page
    """
    _name = "component.request"
    _description = "Component Request"

    name = fields.Char(
        readonly=True,
        default=lambda self: _("New"),
        copy=False,
    )
    user_id = fields.Many2one("res.users", string="Responsible")
    order_line_ids = fields.One2many("component.order.line", "order_id")

    # CRUD methods

    @api.model
    def create(self, vals):
        """
        Used to create sequence number for our request for warranty.
        """
        if vals.get("name", _("New")) == _("New"):
            vals["name"] = self.env["ir.sequence"].next_by_code(
                "component.request.sequence"
            ) or _("New")
        result = super(ComponentRequest, self).create(vals)
        return result
