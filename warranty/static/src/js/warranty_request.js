odoo.define('warranty.warranty', function (require) {
    "use strict"

    var publicWidget = require('web.public.widget')
    var rpc = require('web.rpc')
    publicWidget.registry.WarrantyWidget = publicWidget.Widget.extend({
        selector: '#wrap',
        events: {
            'change select[name="invoice_id"]': 'changeProductField',
            'change select[name="product_id"]': 'changeLotField',
        },

        init: function () {
            this._super.apply(this, arguments)
        },

        changeProductField: async function () {
            var products = await rpc.query({
                model: "account.move.line",
                method: 'search_read',
                fields: ["product_id"],
                domain: [
                    ['move_id', "=", parseInt($('#invoice_id').val())],
                    ['product_id', '!=', false],
                ],
            })
            var product_ids = products.map(function (product) {
                return [product.product_id[0], product.product_id[1]];
            });
            this.renderProductOptions(product_ids);
        },

        changeLotField: async function () {
            var lot_numbers = await rpc.query({
                model: "stock.lot",
                method: 'search_read',
                fields: ["id", "name"],
                domain: [
                    ['product_id', "=", parseInt($('#product_id').val())],
                ],
            })
            var lot_number_ids = lot_numbers.map(function (lot) {
                return [lot.id, lot.name]
            })
            this.renderLotOptions(lot_number_ids)
        },

        renderProductOptions: function (product_ids) {
            $('#product_id').empty().append("<option value=''></option>")
            product_ids.forEach(function (product) {
                $("#product_id").append("<option value='" + product[0] + "'>" + product[1] + "</option>");
            })
        },

        renderLotOptions: function (lot_number_ids) {
            $('#lot_number_id').empty().append("<option value=''></option>")
            lot_number_ids.forEach(function (lot) {
                $("#lot_number_id").append("<option value='" + lot[0] + "'>" + lot[1] + "</option>");
            })
        },
    })
})
