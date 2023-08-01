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
        help="Sequence number"
    )
    user_id = fields.Many2one(
        "res.users", string="Responsible", help="Person responsible for the "
                                                "request")
    order_line_ids = fields.One2many("component.order.line", "order_id")
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("to_approve", "To Approve"),
            ("approved", "Approved"),
            ("cancelled", "Cancelled")
        ],
        default="draft",
        help="Status of the request"
    )

    # CRUD Methods

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

    def create_rfq(self):
        """
        Used to create rfq for different vendors
        """
        for record in self.order_line_ids:
            if record.transfer_type == "purchase":
                for rec in record.product_id.seller_ids:
                    purchase_order = self.env["purchase.order"].create({
                        "partner_id": rec.partner_id.id,
                    })
                    purchase_order.update({
                        "order_line": [(fields.Command.create({
                            "product_id": record.product_id.id,
                            "product_qty": record.quantity,
                            "price_unit": rec.price
                        }))],
                    })
            else:
                stock_picking = self.env["stock.picking"].create({
                    'location_id': record.source_location.id,
                    'location_dest_id': record.destination_location.id,
                    'picking_type_id': self.env["stock.picking.type"].search(
                        [('sequence_code', '=', 'INT')]
                    ).id,
                    'origin': self.name,
                })
                stock_picking.update({
                    "move_ids": [(fields.Command.create({
                        'product_id': record.product_id.id,
                        'location_id': record.source_location.id,
                        'location_dest_id': record.destination_location.id,
                        'name': record.product_id.name,
                        'product_uom_qty': record.quantity,
                    }))],
                })
                stock_picking.action_confirm()

    # Action Methods

    def action_to_approve(self):
        """
        Used to set draft to to_approve state
        """
        self.ensure_one()
        self.state = 'to_approve'

    def action_confirm(self):
        """
        Used to confirm the component request.
        """
        self.ensure_one()
        self.create_rfq()
        self.state = "approved"

    def action_cancel(self):
        """
        Used to reject the component request.
        """
        self.ensure_one()
        self.state = 'cancelled'
