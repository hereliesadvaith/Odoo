/* @odoo-module */
import {InventoryCard} from './inventory_card'
import { useBus, useService } from "@web/core/utils/hooks";
import {registry} from '@web/core/registry';
const { Component, useState, onWillStart } = owl;
const rpc = require('web.rpc')
export class InventoryDashboard extends Component {
    setup() {
        this.orm = useService("orm");
       onWillStart(async () => {
           await this.loadDashboardData();
       });
    }
    async loadDashboardData() {
        const context = {};
        this.product_details = await this.orm.call(
           'product.product',
           'get_stocks',
           [0],
           {
               context: context
           }
       )
    }
}
// Adding to client action to registry.
registry.category("actions").add("inventory_dashboard", InventoryDashboard)
// Adding template.
InventoryDashboard.template = "inventory_dashboard.InventoryDashboard"
// Adding components
InventoryDashboard.components = {InventoryCard}