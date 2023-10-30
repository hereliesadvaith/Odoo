/**@odoo-module **/

import Registries from "point_of_sale.Registries"
import PosComponent from "point_of_sale.PosComponent"
const { onMounted } = owl

class ProductListScreen extends PosComponent {
    setup() {
        super.setup()
        onMounted(() => {
            this.env.posbus.on("renderProduct", this, this.updateProduct)
        })
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
    updateProduct(ev) {
        var product = this.props.products.filter(
            obj => obj.id == ev.values.id
        )
        if (ev.values.img) {
            var $image_div = $("#" + ev.values.id + " td:first")
            $image_div.empty()
            $image_div.append(
                "<div class='product_img'><img src=" + ev.values.img + " style='max-width: 128px; max-height: 128px;'/></div>"
            )
        }
        if (ev.values.default_code) {
            product[0].default_code = ev.values.default_code
        }
        if (ev.values.lst_price) {
            product[0].lst_price = ev.values.lst_price
        }
        if (ev.values.name) {
            product[0].display_name = ev.values.name
        }
        if (ev.values.pos_categ_id && ev.values.pos_categ_id !== 0) {
            product[0].pos_categ_id = [ev.values.pos_categ_id, this.env.pos.db.category_by_id[
                ev.values.pos_categ_id]["name"]]
            console.log(product[0].pos_categ_id)
        }
        if (ev.values.barcode) {
            product[0].barcode = ev.values.barcode
        }
    }
}

ProductListScreen.template = "ProductListScreen";
Registries.Component.add(ProductListScreen);
