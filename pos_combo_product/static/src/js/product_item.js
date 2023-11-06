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
                // combo details
                var combo_products = this.env.pos.combo_product.filter(
                    item => this.props.product.combo_product_ids.includes(item.id)
                )
                // products
                var products = []
                for (var rec of combo_products) {
                    for (var id in rec['product_ids']) {
                        this.env.pos.db.product_by_id[rec[
                            'product_ids'][id]]["parent_product_id"] = this.props.product.id
                        this.env.pos.db.product_by_id[rec[
                            'product_ids'][id]]["combo_quantity"] = rec.quantity
                        this.env.pos.db.product_by_id[rec[
                            'product_ids'][id]]["combo_is_required"] = rec.is_required
                        this.env.pos.db.product_by_id[rec[
                                'product_ids'][id]]["image_url"] = `/web/image?model=product.product&field=image_128&id=${rec['product_ids'][id]}`
                        products.push(this.env.pos.db.product_by_id[rec['product_ids'][id]])
                    }
                }
                // Splitting products based on combo_is_required attribute
                var productsWithComboRequired = products.filter(product => product.combo_is_required)
                var productsWithoutComboRequired = products.filter(product => !product.combo_is_required)

                // Extracting category IDs for each list
                var categoryIdsWithComboRequired = productsWithComboRequired.map(product => product.pos_categ_id[0])
                var categoryIdsWithoutComboRequired = productsWithoutComboRequired.map(product => product.pos_categ_id[0])

                // Creating two dictionaries of categories based on the category IDs
                var categoriesWithComboRequired = Object.values(this.env.pos.db.category_by_id).filter(
                    category => categoryIdsWithComboRequired.includes(category.id)
                )

                var categoriesWithoutComboRequired = Object.values(this.env.pos.db.category_by_id).filter(
                    category => categoryIdsWithoutComboRequired.includes(category.id)
                )
                this.showPopup("ComboProductPopup", {
                    "categoriesWithComboRequired": categoriesWithComboRequired,
                    "productsWithComboRequired": productsWithComboRequired,
                    "categoriesWithoutComboRequired": categoriesWithoutComboRequired,
                    "productsWithoutComboRequired": productsWithoutComboRequired,
                    "products": products,
                })
            }
        }
    }
Registries.Component.extend(ProductItem, ComboProduct)
return ProductItem