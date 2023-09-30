# -*- coding: utf-8 -*-
from odoo import http, fields
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):
    """
    To inherit /shop/cart controller
    """

    @http.route([
        '/shop/cart',
    ], type='http', auth="public", website=True,
        sitemap=False)
    def cart(self, access_token=None, revive='', **post):
        """
        To inherit /shop/cart route
        """
        result = super(WebsiteSale, self).cart(access_token=access_token,
                                               revive=revive, **post)
        bom_components = []
        product_ids = [i.bom_product_ids for i in
                       request.env['website'].sudo().browse(
                           request.website.id
                       )]
        tmpl_ids = [i.product_tmpl_id.id for i in product_ids[0]]
        for record in result.qcontext['website_sale_order'].website_order_line:
            bom_id = request.env['mrp.bom'].sudo().search([
                ('product_tmpl_id', '=', record.product_id.product_tmpl_id.id),
                ('product_tmpl_id', 'in', tmpl_ids),
            ])
            if bom_id:
                for i in bom_id[0].bom_line_ids:
                    bom_components.append([
                        i.product_id.name, record.product_id])
        result.qcontext['bom_components'] = bom_components
        return result

    @http.route(['/shop/cart/update_json'], type='json', auth="public",
                methods=['POST'], website=True, csrf=False)
    def cart_update_json(
            self, product_id, line_id=None, add_qty=None, set_qty=None,
            display=True,
            product_custom_attribute_values=None,
            no_variant_attribute_values=None, **kw
    ):
        # Your custom code here
        result = super(WebsiteSale, self).cart_update_json(
            product_id=product_id,
            line_id=line_id,
            add_qty=add_qty,
            set_qty=set_qty,
            display=display,
            product_custom_attribute_values=product_custom_attribute_values,
            no_variant_attribute_values=no_variant_attribute_values,
            **kw
        )
        print(result)
        bom_components = []
        order = request.website.sale_get_order()
        for record in order.website_order_line:
            bom_id = request.env['mrp.bom'].sudo().search([
                ('product_tmpl_id', '=', record.product_id.product_tmpl_id.id),
            ])
            if bom_id:
                for i in bom_id[0].bom_line_ids:
                    bom_components.append([
                        i.product_id.name, record.product_id])

        result['website_sale.cart_lines'] = request.env[
            'ir.ui.view']._render_template(
            "website_sale.cart_lines", {
                'website_sale_order': order,
                'date': fields.Date.today(),
                'suggested_products': order._cart_accessories(),
                'bom_components': bom_components
            }
        )
        return result
