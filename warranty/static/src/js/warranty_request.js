odoo.define('warranty.warranty_request', function (require) {
    "use strict";
    const rpc = require('web.rpc')
    if (window.location.pathname === '/warranty_request') {
        $(function () {
            var customer_id = $('#customer_id').val()
            $('#invoice_id').on('change', function () {
                changeProductField()
            })
            $('#product_id').on('change', function () {
                changeLotField()
            })
        })
    }
    async function changeProductField () {
        var products = await rpc.query({
            model: "account.move.line",
            method: 'search_read',
            fields: ["product_id"],
            domain: [
            ['move_id', "=", parseInt($('#invoice_id').val())],
            ['product_id', '!=', false],
            ]
        })
        var product_ids = []
        for (var i = 0; i < products.length; i++) {
            product_ids.push(products[i].product_id)
        }
        $('#product_id').empty()
        $('#product_id').append("<option value=''/>")
        for (var i = 0; i < product_ids.length; i++) {
            $("#product_id").append("<option value='" + product_ids[i][0] + "'>" + product_ids[i][1] + "</option>")
        }
    }
    async function changeLotField () {
        var lot_numbers = await rpc.query({
            model: "stock.lot",
            method: 'search_read',
            fields: ["id", "name"],
            domain: [
            ['product_id', "=", parseInt($('#product_id').val())],
            ]
        })
        var lot_number_ids = []
        for (var i = 0; i < lot_numbers.length; i++) {
            lot_number_ids.push([lot_numbers[i].id, lot_numbers[i].name])
        }
        console.log(lot_number_ids)
        $('#lot_number_id').empty()
        $('#lot_number_id').append("<option value=''/>")
        for (var i = 0; i < lot_number_ids.length; i++) {
            $("#lot_number_id").append("<option value='" + lot_number_ids[i][0] + "'>" + lot_number_ids[i][1] + "</option>")
        }
    }
})