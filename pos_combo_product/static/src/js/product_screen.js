/**@odoo-module **/

import Registries from "point_of_sale.Registries"
import ProductItem from "point_of_sale.ProductItem"
import { useListener } from "@web/core/utils/hooks"

const ComboProduct = (ProductItem) =>
    class extends ProductItem {
        setup() {
            super.setup()
            useListener('click-product', this.showComboPopup)
        }
        showComboPopup(ev) {
            console.log(this)
        }
    }
Registries.Component.extend(ProductItem, ComboProduct)
return ProductItem