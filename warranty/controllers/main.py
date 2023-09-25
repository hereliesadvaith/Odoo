# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import content_disposition, request
from odoo.tools import html_escape
from odoo.addons.portal.controllers.portal import CustomerPortal, pager


class XLSXReportController(http.Controller):
    """
    xlsx report controller class.
    """
    @http.route('/xlsx_reports', type='http',
                auth='user', methods=['POST'], csrf=False)
    def get_report_xlsx(self, model, options,
                        output_format, report_name, **kw):
        """
        To call the get_report_xlsx function.
        """
        uid = request.session.uid
        report_obj = request.env[model].with_user(uid)
        options = json.loads(options)
        token = 'dummy-because-api-expects-one'
        try:
            if output_format == 'xlsx':
                response = request.make_response(
                    None,
                    headers=[
                        ('Content-Type', 'application/vnd.ms-excel'),
                        ('Content-Disposition',
                            content_disposition(report_name + '.xlsx'))
                    ]
                )
                report_obj.get_xlsx_report(options, response)
            response.set_cookie('fileToken', token)
            return response
        except Exception as e:
            se = http.serialize_exception(e)
            error = {
                'code': 200,
                'message': 'Odoo Server Error',
                'data': se
            }
            return request.make_response(html_escape(json.dumps(error)))


class WarrantyController(http.Controller):
    """
    warranty request page controller class
    """
    @http.route('/warranty_request', type='http', auth='user',
                website=True)
    def warranty_web_form(self, **kw):
        """
        To return our warranty request page
        """
        invoices = request.env['account.move'].sudo().search([
            ("state", "=", "posted"),
            ("name", "like", "INV"),
            ("partner_id", "=", request.env.user.partner_id.id)
        ])
        products = request.env['product.product'].sudo().search([])
        lot_numbers = request.env['stock.lot'].sudo().search([])
        return http.request.render('warranty.warranty_request', {
            "invoices": invoices,
            "products": products,
            "lot_numbers": lot_numbers,
            "customer_id": request.env.user.partner_id,
        })

    @http.route('/create/warranty_request', type="http", auth='user',
                website=True)
    def create_warranty_request(self, **kw):
        """
        To add warranty request data to backend.
        """
        kw.pop("customer_id")
        request.env['request.for.warranty'].sudo().create(kw)
        return http.request.render('warranty.customer_thanks')


class PortalWarranty(CustomerPortal):
    """
    Warranty request page inside account documents page.
    """
    def _prepare_home_portal_values(self, counters):
        """
        To get the count of the warranties in portal
        """
        values = super(PortalWarranty, self)._prepare_home_portal_values(
            counters)
        warranties_count = request.env['request.for.warranty'].search_count(
            [('customer_id', '=', request.env.user.partner_id.id)]
        )
        values.update({
            'warranties_count': warranties_count
        })
        return values

    @http.route(['/my/warranties', '/my/warranties/page/<int:page>'],
                type='http', auth="user", website=True)
    def warranty_pagination_view(self, page=1, **kwargs):
        """
        To get the warranty details to warranty page.
        """
        warranties_count = request.env['request.for.warranty'].search_count(
            [('customer_id', '=', request.env.user.partner_id.id)]
        )
        page_detail = pager(url='/my/warranties', total=warranties_count,
                            page=page, step=10)
        warranties = request.env['request.for.warranty'].search([
            ('customer_id', '=', request.env.user.partner_id.id)
        ], limit=10, offset=page_detail['offset'])
        values = {
            'warranties': warranties,
            'page_name': 'warranties',
            'pager': page_detail,
        }
        return request.render('warranty.portal_my_warranties', values)
