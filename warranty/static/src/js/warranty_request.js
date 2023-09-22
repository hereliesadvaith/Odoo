odoo.define('warranty.warranty_request', function (require) {
    "use strict";
    const rpc = require('web.rpc')
    if (window.location.pathname === '/warranty_request') {
        $(function () {
            var customer_id = $('#customer_id').val()
            $('#invoice_id').on('change', function () {
                var products = changeSelectField()
                $('#product_id').empty()
                console.log(products)
            })
        })
    }
    async function changeSelectField () {
        var result = await rpc.query({
            model: "account.move.line",
            method: 'search_read',
            fields: ["id"],
            domain: [['move_id', "=", parseInt($('#invoice_id').val())]]
        })
        return result
    }
})