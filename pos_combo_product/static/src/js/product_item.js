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
                // combo_details
                var combo_products = this.env.pos.combo_product.filter(
                    product => this.props.product.combo_product_ids.includes(product.id)
                )
                var product_ids = []
                for (var rec of combo_products) {
                    for (var id in rec['product_ids']) {
                        product_ids.push(rec['product_ids'][id])
                    }
                }
                // products
                var products = Object.values(this.env.pos.db.product_by_id).filter(
                    product => product_ids.includes(product.id)
                )
                // categories
                var categories = []
                for (var rec of products) {
                    categories.push(rec.pos_categ_id[1])
                }
                for (var rec of products) {
                    rec["image_url"] = `/web/image?model=product.product&field=image_128&id=${rec.id}`
                }
                this.showPopup("ComboProductPopup", {
                    "categories": categories,
                    "combo_product_ids": this.props.product.combo_product_ids,
                    "product": this.props.product,
                })
            }
        }
    }
Registries.Component.extend(ProductItem, ComboProduct)
return ProductItem