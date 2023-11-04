/**@odoo-module **/

import AbstractAwaitablePopup from "point_of_sale.AbstractAwaitablePopup"
import Registries from "point_of_sale.Registries"


class ComboProductPopup extends AbstractAwaitablePopup {
    setup() {
        super.setup()
    }
    addToOrderLine(ev) {
        console.log(ev.currentTarget.dataset.product)
    }
    confirm() {
        this.env.posbus.trigger('close-popup', {
            popupId: this.props.id,
            response: { confirmed: false, payload: null },
        })
    }
}

ComboProductPopup.template = "ComboProductPopup"
Registries.Component.add(ComboProductPopup)
