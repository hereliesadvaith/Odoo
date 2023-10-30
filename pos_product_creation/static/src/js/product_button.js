/** @odoo-module **/

const PosComponent = require('point_of_sale.PosComponent')
const ProductScreen = require('point_of_sale.ProductScreen')
const Registries = require('point_of_sale.Registries')
const { useListener } = require('@web/core/utils/hooks')

class OpenProductListButton extends PosComponent {
    setup () {
        super.setup()
        useListener('click', this.openProductList)
    }

    async openProductList () {
        var products = await this.env.pos.db.product_by_id
        var productsList = []
        for (var key in products) {
            products[key]["image_url"] = `/web/image?model=product.product&field=image_128&id=${products[key].id}`
            productsList.push(products[key])
        }
        this.showScreen("ProductListScreen", {
            "products": productsList,
        })
    }
}

OpenProductListButton.template = "OpenProductListButton"
ProductScreen.addControlButton({
    component: OpenProductListButton,
    position: ['before', 'OrderlineCustomerNoteButton'],
})

Registries.Component.add(OpenProductListButton)
return OpenProductListButton
