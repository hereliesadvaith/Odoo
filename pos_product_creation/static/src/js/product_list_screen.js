/**@odoo-module **/

import Registries from "point_of_sale.Registries";
import PosComponent from "point_of_sale.PosComponent";

class ProductListScreen extends PosComponent {
    setup() {
        super.setup()
    }
    createProduct() {
        this.showPopup("CreateProductPopup")
    }
    discard() {
        this.showScreen("ProductScreen")
    }
    editProduct(ev) {
        var product = this.props.products.filter(
            obj => obj.id == ev.target.dataset.productId)
        this.showPopup("EditProductPopup", {
            "product": product[0],
        })
    }
}

ProductListScreen.template = "ProductListScreen";
Registries.Component.add(ProductListScreen);
