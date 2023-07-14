# -*- coding: utf-8 -*-

from odoo import fields, models


class WarrantyType(models.Model):
    """
    This class is used to make the Warranty Type.
    """

    _name = "warranty.type"
    _description = "Warranty Type"

    name = fields.Char(required=True)
