# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class WebsiteTracking(http.Controller):
    """
    To inherit add values in website tracking page
    """
    @http.route(['/order_tracking/<int:order_id>'],
                type='http', auth="public", website=True)
    def warranties_form_view(self, **kwargs):
        """
        To get the order tracking page.
        """
        order = request.env['sale.order'].browse(kwargs['order_id'])
        transfers = request.env['stock.picking'].search([
            ('origin', '=', order.name)
        ])[0].track_order_ids
        print(transfers)
        values = {
            "transfers": transfers,
            "order": order,
        }
        return request.render('website_order_tracking.order_tracking', values)
