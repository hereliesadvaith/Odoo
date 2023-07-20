# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.tools import date_utils


class RequestForWarranty(models.Model):
    """
    This class is used to make the model of our Request For Warranty page
    """

    _name = "request.for.warranty"
    _description = "Request For Warranty"

    name = fields.Char(
        required=True,
        readonly=True,
        index=True,
        default=lambda self: _("New"),
        copy=False,
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
        string="Purchase Date", related="invoice_id.invoice_date"
    )
    warranty_type = fields.Selection(
        string="Warranty Type",
        selection=[
            ("service_warranty", "Service Warranty"),
            ("replacement_warranty", "Replacement Warranty"),
        ],
        related="product_id.warranty_type",
    )
    warranty_period = fields.Integer(
        string="Warranty Period(Days)", related="product_id.warranty_period"
    )
    warranty_expire_date = fields.Date(
        string="Warranty Expire Date", compute="_compute_warranty_expire_date"
    )
    delivery_count = fields.Integer(string="Delivery Count", default=0)

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
                record.product_id.id for record in self.invoice_id.invoice_line_ids
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

    def transfer_from_customer(self):
        """
        Used to create a transfer in stock picking.
        """
        customer_location = self.env.ref("stock.stock_location_customers").id
        warranty_location = self.env.ref("warranty.warranty_location").id
        picking_type = self.env.ref("stock.picking_type_in").id
        partner = self.customer_id.id
        origin = self.name
        uom_id = self.product_id.uom_id.id
        lot_id = self.lot_number_id.id
        product_id = self.product_id.id
        self.env["stock.picking"].create(
            {
                "location_id": customer_location,
                "location_dest_id": warranty_location,
                "picking_type_id": picking_type,
                "partner_id": partner,
                "origin": origin,
            }
        )
        pick_last_id = self.env["stock.picking"].search([], order="id desc")[0]
        self.env["stock.move.line"].create(
            {
                "picking_id": pick_last_id.id,
                "product_id": product_id,
                "product_uom_id": uom_id,
                "lot_id": lot_id,
                "location_id": customer_location,
                "location_dest_id": warranty_location,
                "reserved_uom_qty": 1,
            }
        )
        move_last_id = self.env["stock.move"].search([], order="id desc")[0]
        move_last_id.write(
            {
                "product_uom_qty": 1,
            }
        )
        pick_last_id.state = "assigned"

    def transfer_to_customer(self):
        """
        To create a delivery transfer to customer.
        """
        if self.product_id.warranty_type == "service_warranty":
            warranty_location = self.env.ref("warranty.warranty_location").id
        else:
            warranty_location = self.env.ref("stock.stock_location_stock").id
        customer_location = self.env.ref("stock.stock_location_customers").id
        picking_type = self.env.ref("stock.picking_type_out").id
        partner = self.customer_id.id
        origin = self.name
        uom_id = self.product_id.uom_id.id
        lot_id = self.lot_number_id.id
        product_id = self.product_id.id
        self.env["stock.picking"].create(
            {
                "location_id": warranty_location,
                "location_dest_id": customer_location,
                "picking_type_id": picking_type,
                "partner_id": partner,
                "origin": origin,
            }
        )
        pick_last_id = self.env["stock.picking"].search([], order="id desc")[0]
        self.env["stock.move.line"].create(
            {
                "picking_id": pick_last_id.id,
                "product_id": product_id,
                "product_uom_id": uom_id,
                "lot_id": lot_id,
                "location_id": warranty_location,
                "location_dest_id": customer_location,
            }
        )
        move_last_id = self.env["stock.move"].search([], order="id desc")[0]
        move_last_id.write(
            {
                "product_uom_qty": 1,
            }
        )
        pick_last_id.state = "assigned"

    # Action methods

    def action_to_approve(self):
        """
        To check if the product have a warranty and confirm Request for warranty
        """
        self.ensure_one()
        self.state = "to_approve"
        # locations = self.env["stock.location"].search([])
        # for i in locations:
        #     print(i.get_metadata()[0].get('xmlid'))
        # warranty_location = self.env.ref('stock.stock_location_stock').id
        # print(warranty_location)

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
        self.transfer_from_customer()
        self.state = "approved"
        self.delivery_count += 1

    def action_return(self):
        """
        To create a delivery transfer to customer.
        """
        self.ensure_one()
        self.transfer_to_customer()
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
