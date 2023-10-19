/* @odoo-module */
import {registry} from '@web/core/registry';
const {Component} = owl
export class InventoryDashboard extends Component {
    setup() {
        console.log("hi")
    }
}
registry.category("actions").add("inventory_dashboard", InventoryDashboard)
InventoryDashboard.template = "inventory_dashboard.InventoryDashboard"