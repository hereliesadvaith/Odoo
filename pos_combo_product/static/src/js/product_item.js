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
        showComboPopup() {
            if (this.props.product.is_combo) {
                const categories = Object.keys(
                    this.env.pos.db.category_by_id
                    ).map(key => this.env.pos.db.category_by_id[key])
                this.showPopup("ComboProductPopup", {
                    "categories": categories,
                    "combo_product_ids": this.props.product.combo_product_ids,
                })
            }
        }
    }
Registries.Component.extend(ProductItem, ComboProduct)
return ProductItem