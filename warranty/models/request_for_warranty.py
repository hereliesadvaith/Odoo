# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.tools import date_utils


class RequestForWarranty(models.Model):
    """
    This class is used to make the model of our Request For Warranty page
    """
    _name = "request.for.warranty"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Request For Warranty"

    name = fields.Char(
        readonly=True,
        default=lambda self: _("New"),
        copy=False,
        help="Sequence number of request"
    )
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("to_approve", "To Approve"),
            ("approved", "Approved"),
            ("received", "Product Received"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
        help="Status of the request"
    )
    invoice_id = fields.Many2one(
        "account.move",
        string="Invoice",
        required=True,
        domain=[("state", "=", "posted"), ("name", "like", "INV")],
        help="Invoice number"
    )
    product_id = fields.Many2one(
        "product.product", string="Product", required=True, help="Product")
    lot_number_id = fields.Many2one(
        "stock.lot", string="Lot/Serial Number", help="Lot or Serial number "
                                                      "of the product")
    request_date = fields.Date(
        default=fields.Date.today(), help="Date of the request")
    customer_id = fields.Many2one(
        "res.partner", string="Customer", related="invoice_id.partner_id",
        tracking=True,
        help="Customer"
    )
    purchase_date = fields.Date(
        string="Purchase Date", related="invoice_id.invoice_date",
        help="Purchased date"
    )
    warranty_type = fields.Selection(
        string="Warranty Type",
        selection=[
            ("service_warranty", "Service Warranty"),
            ("replacement_warranty", "Replacement Warranty"),
        ],
        related="product_id.warranty_type",
        help="Type of warranty"
    )
    warranty_period = fields.Integer(
        string="Warranty Period(Days)", related="product_id.warranty_period",
        help="Valid period for warranty"
    )
    warranty_expire_date = fields.Date(
        string="Warranty Expire Date", compute="_compute_warranty_expire_date",
        help="Expiration date of warranty"
    )
    delivery_count = fields.Integer(
        string="Delivery Count", default=0, help="Number of stock moves")

    # Compute functions

    @api.depends("purchase_date", "warranty_period")
    def _compute_warranty_expire_date(self):
        """
        To compute the warranty expiration date
        """
        for record in self:
            if record.warranty_period and record.purchase_date:
                record.warranty_expire_date = date_utils.add(
                    record.purchase_date, days=record.warranty_period
                )
            else:
                record.warranty_expire_date = False

    # Onchange functions

    @api.onchange("invoice_id")
    def _onchange_invoice_id(self):
        """
        Used to make dynamic domain for product_id.
        """
        self.product_id = False
        self.lot_number_id = False
        if self.invoice_id:
            domain_list = [
                record.product_id.id for record in
                self.invoice_id.invoice_line_ids
            ]
            domain = [("id", "in", domain_list), ("has_warranty", "=", True)]
        else:
            domain = []
        return {"domain": {"product_id": domain}}

    @api.onchange("product_id")
    def _onchange_product_id(self):
        """
        Used to make dynamic domain for lot_number.
        """
        self.lot_number_id = False
        if self.product_id:
            domain = [("product_id", "=", self.product_id.id)]
        else:
            domain = []
        return {"domain": {"lot_number_id": domain}}

    # CRUD methods

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

    def transfer(self, location_id, location_dest_id, picking_type):
        """
        Used to create a transfer in stock picking.
        """
        stock_picking = self.env["stock.picking"].create({
            'location_id': location_id,
            'location_dest_id': location_dest_id,
            'picking_type_id': picking_type,
            'partner_id': self.customer_id.id,
            'origin': self.name,
        })
        self.env["stock.move"].create({
            'product_id': self.product_id.id,
            'location_id': location_id,
            'location_dest_id': location_dest_id,
            'picking_id': stock_picking.id,
            'name': self.product_id.name,
            'quantity_done': 1,
        })
        stock_picking.action_confirm()
        stock_picking.button_validate()

    # Action methods

    def action_to_approve(self):
        """
        To check if the product have a warranty and confirm Request for warranty
        """
        self.ensure_one()
        self.state = "to_approve"

    def action_cancel(self):
        """
        To cancel request for warranty
        """
        self.ensure_one()
        self.state = "cancelled"

    def action_confirm(self):
        """
        To approve request for warranty
        """
        self.ensure_one()
        location_id = self.env.ref("stock.stock_location_customers").id
        location_dest_id = self.env.ref("warranty.warranty_location").id
        picking_type = self.env.ref("stock.picking_type_in").id
        self.transfer(location_id, location_dest_id, picking_type)
        self.state = "received"
        self.delivery_count += 1

    def action_return(self):
        """
        To create a delivery transfer to customer.
        """
        self.ensure_one()
        if self.product_id.warranty_type == "service_warranty":
            location_id = self.env.ref("warranty.warranty_location").id
        else:
            location_id = self.env.ref("stock.stock_location_stock").id
        location_dest_id = self.env.ref("stock.stock_location_customers").id
        picking_type = self.env.ref("stock.picking_type_out").id
        self.transfer(location_id, location_dest_id, picking_type)
        self.state = 'done'
        self.delivery_count += 1

    def action_view_stock_moves(self):
        """
        To see the stock moves related to warranty.
        """
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Transfers",
            "view_mode": "tree,form",
            "res_model": "stock.picking",
            "context": "{'create': False}",
            "domain": [("origin", "=", self.name)],
        }
