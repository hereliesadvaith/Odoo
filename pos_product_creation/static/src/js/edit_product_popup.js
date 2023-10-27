/**@odoo-module **/

import AbstractAwaitablePopup from "point_of_sale.AbstractAwaitablePopup";
import Registries from "point_of_sale.Registries";
import { useListener } from "@web/core/utils/hooks";

let base64_img = ""

class EditProductPopup extends AbstractAwaitablePopup {
    setup() {
        super.setup();
    }
}

EditProductPopup.template = "EditProductPopup";
Registries.Component.add(EditProductPopup);
