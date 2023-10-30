/**@odoo-module **/

import AbstractAwaitablePopup from "point_of_sale.AbstractAwaitablePopup";
import Registries from "point_of_sale.Registries";
import { useListener } from "@web/core/utils/hooks";

let base64_img = ""

class CreateProductPopup extends AbstractAwaitablePopup {
    setup() {
        super.setup();
        useListener("change", "#img_field", this.onChangeImgField);
    }
    async onChangeImgField(ev) {
        let current = ev.target.files[0]
        const reader = new FileReader()
        reader.readAsDataURL(current)
        reader.onload =  await function () {
            base64_img = reader.result.toString().replace(/^data:(.*,)?/, "")
        }
    }
    async confirm () {
        let values = {}
        let name = $("#display_name").val()
        let price = $("#list_price").val()
        let cost = $("#cost_price").val()
        let category = $("#product_category").val()
        let barcode = $("#barcode").val()
        let default_code = $("#default_code").val()
        if (name && price) {
            values["name"] = name
            values["lst_price"] = price
            if (base64_img) {
                values["image_1920"] = base64_img
            }
            if (cost) {
                values["standard_price"] = cost
            }
            if (category) {
                values["pos_categ_id"] = category
            }
            if (barcode) {
                values["barcode"] = barcode
            }
            if (default_code) {
                values["default_code"] = default_code
            }
            values["available_in_pos"] = true;
            await this.rpc({
                model: "product.product",
                method: "create",
                args: [values],
            })
            this.env.posbus.trigger('close-popup', {
                popupId: this.props.id,
                response: { confirmed: false, payload: null },
            })
        }
        window.location.reload()
    }
}

CreateProductPopup.template = "CreateProductPopup"
Registries.Component.add(CreateProductPopup)