odoo.define('warranty.warranty', function (require) {
    "use strict"

    var publicWidget = require('web.public.widget')
    var rpc = require('web.rpc')
    publicWidget.registry.WarrantyWidget = publicWidget.Widget.extend({
        selector: '.warranty_form',
        events: {
            'change select[name="invoice_id"]': 'changeProductField',
            'change select[name="product_id"]': 'changeLotField',
        },
        //        init: function () {
        //            this._super.apply(this, arguments)
        //        }, use this when you have to write init functions
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
            this.$el.find('select[name="product_id"]').empty().append("<option value=''></option>");
            product_ids.forEach(function (product) {
                this.$el.find('select[name="product_id"]').append("<option value='" + product[0] + "'>" + product[1] + "</option>");
            }.bind(this))
        },
        renderLotOptions: function (lot_number_ids) {
            this.$el.find('select[name="lot_number_id"]').empty().append("<option value=''></option>");
            lot_number_ids.forEach(function (lot) {
                this.$el.find('select[name="lot_number_id"]').append("<option value='" + lot[0] + "'>" + lot[1] + "</option>");
            }.bind(this))
        },
    })
})

odoo.define('warranty.warranty_snippet', function (require) {
    var PublicWidget = require('web.public.widget')
    var rpc = require('web.rpc')
    var core = require('web.core')
    var qweb = core.qweb
    var warrantySnippet = PublicWidget.Widget.extend({
        selector: '.warranty_snippet',
        events: {
            'click .carousel-control-next': 'carouselNext',
            'click .carousel-control-prev': 'carouselPrev',
        },
        start: function () {
            var self = this;
            rpc.query({
                route: '/latest_warranties',
                params: {},
            }).then(function (result) {
                result.forEach(function (warranty) {
                    var customer = warranty['customer_id'][1].includes(',') ? warranty['customer_id'][1].split(',')[1] : warranty['customer_id'][1]
                    var product = warranty['product_id'][1].includes(']') ? warranty['product_id'][1].split(']')[1] : warranty['product_id'][1]
                    warranty['customer_id'][1] = customer
                    warranty['product_id'][1] = product
                    warranty['href'] = "/my/warranties/"+ warranty['id']
                })
                var chunks = _.chunk(result, 4)
                chunks[0].is_active = true
                self.$("#warranty_carousel").html(
                    qweb.render('warranty.warranty_snippet_carousel', {chunks})
                )
            })
        },
        carouselNext: function (event) {
            var buttons = this.$('.carousel-control-next')
            for (var i = 0; i < buttons.length; i++) {
                buttons.eq(i).data('slNo', i)
            }
            var nextValue = $(event.currentTarget).data('slNo')
            this.$('.carousel').eq(nextValue).carousel('next')
        },
        carouselPrev: function (event) {
            var buttons = this.$('.carousel-control-prev')
            for (var i = 0; i < buttons.length; i++) {
                buttons.eq(i).data('slNo', i)
            }
            var prevValue = $(event.currentTarget).data('slNo')
            this.$(".carousel").eq(prevValue).carousel('prev')
        },
    });
    PublicWidget.registry.warranty_snippet = warrantySnippet
    return warrantySnippet
});