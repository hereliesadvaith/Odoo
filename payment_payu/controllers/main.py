# -*- coding: utf-8 -*-
from odoo.http import Controller, request, route


class PayUController(Controller):
    """
    Controller for PayU payment return pages.
    """
    _return_url = '/payment/payu/return'

    @route(_return_url, type="http", auth="public",
                methods=['POST'], csrf=False, save_session=False)
    def payu_return(self, **kw):
        """
        Process the data send by PayU after redirection.
        """
        transaction_id = request.env['payment.transaction'].sudo().search(
            [('transaction_id', '=', kw['txnid'])]
        )
        if kw['status'] == 'success':
            transaction_id._set_done()
        return request.redirect('payment/status')
