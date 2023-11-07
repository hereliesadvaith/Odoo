/**@odoo-module **/

import Registries from "point_of_sale.Registries"
import Orderline from "point_of_sale.Orderline"
const { onMounted } = owl

const ComboProductline = (Orderline) =>
    class extends Orderline {
        setup() {
            super.setup()
            if (!this.props.line.combo_products) {
                this.props.line.combo_products = []
            }
            onMounted(() => {
                this.env.posbus.on("addToOrderLine", this, this.addToOrderLine)
                this.env.posbus.on("removeFromOrderLine", this, this.removeFromOrderLine)
            })
        }
        addToOrderLine(ev) {
            if (this.props.line.product.id == ev.product.parent_product_id) {
                this.props.line.combo_products.push(ev.product)
            }
        }
        removeFromOrderLine(ev) {
            if (this.props.line.product.id == ev.product.parent_product_id) {
                // this.props.line.combo_products.push(ev.product)
                const index = this.props.line.combo_products.findIndex(product => product.id === ev.product.id)
                if (index !== -1) {
                    this.props.line.combo_products.splice(index, 1)
                }
            }
        }
    }
Registries.Component.extend(Orderline, ComboProductline)
return ComboProductline