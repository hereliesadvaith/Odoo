from odoo import http
from odoo.http import request


class WarrantySnippet(http.Controller):
    """
    To change the values of snippet view
    """
    @http.route(['/latest_warranties'], type="json", auth="public")
    def latest_warranties(self):
        """
        To return the values for snippet
        """
        warranties = request.env['request.for.warranty'].search_read(
            [], order="request_date desc", limit=4
        )
        return warranties
