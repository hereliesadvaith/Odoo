/** @odoo-module **/
import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"
const { Component } = owl


class QRCode extends Component {
    setup(){
        // Functions that works at setup
        super.setup(...arguments)
        this.action = useService("action")
    }
    _onClick() {
        // To pop up wizard when clicking on the QR Code button
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "QR Code Generator",
            res_model: "qr.code.generator",
            view_mode: "form",
            views: [[false, "form"]],
            target: "new",
        })
    }
}
QRCode.template = "qr_code_generator";
const Systray = {
    Component: QRCode,
}
registry.category("systray").add("qr_code_generator", Systray)
