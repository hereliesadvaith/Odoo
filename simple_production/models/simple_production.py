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
    product_id = fields.Many2one("product.product", string="Product")
    quantity = fields.Integer(string="Quantity", default=1)
    component_ids = fields.One2many("required.component",
                                    "simple_production_id",
                                    readonly=False)
    state = fields.Selection([('draft', 'Draft'), ('post', 'Post'),
                              ('done', 'Done'), ('cancelled', 'Cancelled')], default="draft")

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
        Used to set draft to to_approve state
        """
        self.ensure_one()
        self.state = 'post'

    def action_done(self):
        """
        Used to confirm the component request.
        """
        self.ensure_one()
        self.state = "done"

    def action_cancel(self):
        """
        Used to reject the component request.
        """
        self.ensure_one()
        self.state = 'cancelled'
