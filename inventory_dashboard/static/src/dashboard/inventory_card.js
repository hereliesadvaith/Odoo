/* @odoo-module */
import {registry} from '@web/core/registry';
const {Component} = owl;
export class InventoryCard extends Component {}
// Adding Template
InventoryCard.template = 'inventory_dashboard.InventoryCard'
InventoryCard.props = ['incoming_stock']