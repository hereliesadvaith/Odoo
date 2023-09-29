odoo.define('cart_bom.bill_of_materials', function (require) {
    "use strict"

    var publicWidget = require('web.public.widget')
    publicWidget.registry.WarrantyWidget = publicWidget.Widget.extend({
        selector: '.js_cart_line',
        events: {
            'change .cart_bom': 'reloadPage',
        },
        reloadPage: function () {
            console.log("hi")
        }
    })
})
