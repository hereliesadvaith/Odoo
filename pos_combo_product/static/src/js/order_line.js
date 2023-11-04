/**@odoo-module **/

import Registries from "point_of_sale.Registries"
import Orderline from "point_of_sale.Orderline"
// import { useListener } from "@web/core/utils/hooks"

const ComboProductline = (Orderline) =>
    class extends Orderline {
        setup() {
            super.setup()
            console.log(this)
        }
    }
Registries.Component.extend(Orderline, ComboProductline)
return ComboProductline