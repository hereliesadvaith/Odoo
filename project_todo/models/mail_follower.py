# -*- coding: utf-8 -*-
from odoo import api, models


class Followers(models.Model):
    """
    To remove unique constrain of mail follower model.
    """
    _inherit = 'mail.followers'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'res_model' in vals and 'res_id' in vals and 'partner_id' in vals:
                dups = self.env['mail.followers'].search([
                    ('res_model', '=', 'todo.task'),
                    ('res_id', '=', vals.get('res_id')),
                    ('partner_id', '=', vals.get('partner_id'))
                ])
                for dup in dups:
                    dup.unlink()
        res = super(Followers, self).create(vals_list)
        return res
    