/**@odoo-module **/

import Registries from "point_of_sale.Registries"
import { Orderline } from "point_of_sale.models"

const ComboProductline = (Orderline) =>
    class ComboProductline extends Orderline {
        constructor() {
            super(...arguments)
        }
        init_from_JSON(json) {
            super.init_from_JSON(...arguments)
            this.combo_products = json.combo_products
        }
        export_as_JSON() {
            var result = super.export_as_JSON(...arguments)
            var combo_products = []
            if (this.combo_products) {
                for (var rec of this.combo_products) {
                    combo_products.push(
                        {
                            "id": rec.id,
                            "display_name": rec.display_name,
                            "combo_quantity": rec.combo_quantity,
                            "lst_price": rec.lst_price,
                        }
                    )
                }
                result.combo_products = combo_products
            }
            return result
        }   
        get_combo_products() {
            return this.combo_products
        }
        export_for_printing() {
            var result = super.export_for_printing(...arguments)
            var combo_products = []
            if (this.combo_products) {
                for (var rec of this.combo_products) {
                    combo_products.push(
                        {
                            "id": rec.id,
                            "display_name": rec.display_name,
                            "combo_quantity": rec.combo_quantity,
                            "lst_price": rec.lst_price,
                        }
                    )
                }
                result.combo_products = combo_products
            }
            return result
        }
    }
Registries.Model.extend(Orderline, ComboProductline)
return Orderline