# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SimpleProduction(models.Model):
    """
    This class is used to make the model of our Request For Warranty page
    """
    _name = "simple.production"
    _description = "Simple Production"

    name = fields.Char(
        readonly=True,
        default=lambda self: _("New"),
        copy=False,
        help="Sequence number"
    )
    product_id = fields.Many2one("product.product",
                                 string="Product",
                                 domain=[("manufacture_ok", "=", True)],
                                 required=True,
                                 help="Product")
    quantity = fields.Integer(string="Quantity", default=1)
    component_ids = fields.One2many("required.component",
                                    "simple_production_id",
                                    readonly=False)
    state = fields.Selection([('draft', 'Draft'), ('post', 'Post'),
                              ('done', 'Done'), ('cancelled', 'Cancelled')],
                             default="draft", help="status")
    delivery_count = fields.Integer(
        string="Delivery Count", default=0, help="Number of stock moves")
    storage_location_id = fields.Many2one("stock.location",
                                          string="Storage Location",
                                          help="Where to store the product")

    # CRUD Methods

    @api.model
    def create(self, vals):
        """
        Used to create sequence number for our request for warranty.
        """
        if vals.get("name", _("New")) == _("New"):
            vals["name"] = self.env["ir.sequence"].next_by_code(
                "simple.production.sequence"
            ) or _("New")
        result = super(SimpleProduction, self).create(vals)
        return result

    # Onchange Methods

    @api.onchange("quantity", "product_id")
    def onchange_quantity(self):
        """
        Used to change the component's quantity.
        """
        self.update({
            "component_ids": [(fields.Command.clear())],
        })
        for record in self.product_id.component_ids:
            self.update({
                "component_ids": [(fields.Command.create({
                    "product_id": record.product_id.id,
                    "quantity": self.quantity * record.quantity,
                }))],
            })

    # Action Methods

    def action_confirm(self):
        """
        Used to set draft to to_approve state and transfer components
        """
        self.ensure_one()
        location_id = self.env.ref("stock.stock_location_stock").id
        location_dest_id = (
            self.env.ref("simple_production.production_location").id)
        for record in self.component_ids:
            stock_picking = self.env["stock.picking"].create({
                'location_id': record.source_location_id.id
                if record.source_location_id else location_id,
                'location_dest_id': location_dest_id,
                'picking_type_id': self.env.ref("stock.picking_type_in").id,
                'origin': self.name,
            })
            stock_picking.update({
                "move_ids": [(fields.Command.create({
                    'product_id': record.product_id.id,
                    'location_id': record.source_location_id.id
                    if record.source_location_id else location_id,
                    'location_dest_id': location_dest_id,
                    'name': record.product_id.name,
                    'quantity_done': record.quantity,
                }))],
            })
            stock_picking.action_confirm()
            stock_picking.button_validate()
            self.delivery_count += 1
        self.state = 'post'

    def action_done(self):
        """
        Used to transfer manufactured product.
        """
        self.ensure_one()
        self.state = "done"
        location_dest_id = self.env.ref("stock.stock_location_stock").id
        location_id = (
            self.env.ref("simple_production.production_location").id)
        stock_picking = self.env["stock.picking"].create({
            'location_id': location_id,
            'location_dest_id': self.storage_location_id.id
            if self.storage_location_id else location_dest_id,
            'picking_type_id': self.env["stock.picking.type"].search(
                [('sequence_code', '=', 'INT')]
            ).id,
            'origin': self.name,
        })
        stock_picking.update({
            "move_ids": [(fields.Command.create({
                'product_id': self.product_id.id,
                'location_id': location_id,
                'location_dest_id': self.storage_location_id.id
                if self.storage_location_id else location_dest_id,
                'name': self.product_id.name,
                'quantity_done': self.quantity,
            }))],
        })
        stock_picking.action_confirm()
        stock_picking.button_validate()
        product = self.env["stock.quant"].search([
            ("location_id", "=", location_id),
            ("product_id", "=", self.product_id.id)
        ])
        product.update({
            "inventory_quantity": product.quantity + self.quantity
        })
        product.action_apply_inventory()
        for record in self.component_ids:
            component_id = self.env["stock.quant"].search([
                ("location_id", "=", location_id),
                ("product_id", "=", record.product_id.id)
            ])
            component_id.update({
                "inventory_quantity": component_id.quantity - record.quantity
            })
            component_id.action_apply_inventory()
        self.delivery_count += 1

    def action_cancel(self):
        """
        Used to reject the component request.
        """
        self.ensure_one()
        self.state = 'cancelled'

    def action_view_stock_moves(self):
        """
        To see the stock moves related to production.
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
