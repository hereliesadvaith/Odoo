# -*- coding: utf-8 -*-
from odoo import fields, models


class RequestForWarranty(models.Model):
    """
    This class is used to make the model of our Request For Warranty page
    """

    _name = "request.for.warranty"
    _description = "Request For Warranty"

    name = fields.Char(required=True)
