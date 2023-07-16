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
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("to_approve", "To Approve"),
            ("approved", "Approved"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
    )
    invoice_id = fields.Many2one(
        "account.move",
        string="Invoice",
        required=True,
        domain=[("state", "=", "posted"), ("name", "like", "INV")],
    )
    product_id = fields.Many2one("product.product", string="Product", required=True)
    lot_number_id = fields.Many2one("stock.lot", string="Lot/Serial Number")
    request_date = fields.Date(default=fields.Date.today())
    customer_id = fields.Many2one(
        "res.partner", string="Customer", related="invoice_id.partner_id"
    )
    purchase_date = fields.Date(
        string="Puchase Date", related="invoice_id.invoice_date"
    )
    warranty_type_id = fields.Many2one(
        "warranty.type", string="Warranty Type", related="product_id.warranty_type_id"
    )
    warranty_period = fields.Integer(
        string="Warranty Period(Days)", related="product_id.warranty_period"
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
