/**@odoo-module **/

import Registries from "point_of_sale.Registries"
import Orderline from "point_of_sale.Orderline"
const { onMounted } = owl

const ComboProductline = (Orderline) =>
    class extends Orderline {
        setup() {
            super.setup()
            if (!this.props.combo_products) {
                this.props.combo_products = []
            }
            onMounted(() => {
                this.env.posbus.on("addToOrderLine", this, this.addToOrderLine)
            })
        }
        addToOrderLine(ev) {
            this.props.combo_products.push(ev.product)
            console.log(this.props)
        }
    }
Registries.Component.extend(Orderline, ComboProductline)
return ComboProductline