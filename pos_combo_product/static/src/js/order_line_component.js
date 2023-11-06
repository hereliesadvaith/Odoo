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
            })
        }
        addToOrderLine(ev) {
            if (this.props.line.product.id == ev.product.parent_product_id) {
                this.props.line.combo_products.push(ev.product)
            }
        }
    }
Registries.Component.extend(Orderline, ComboProductline)
return ComboProductline