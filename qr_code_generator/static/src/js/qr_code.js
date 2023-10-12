/** @odoo-module **/
import { registry } from "@web/core/registry"
const { Component } = owl

class QRCode extends Component {

}
QRCode.template = "qr_code_generator";
const Systray = {
    Component: QRCode,
}
registry.category("systray").add("qr_code_generator", Systray)