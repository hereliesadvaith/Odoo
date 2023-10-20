/* @odoo-module */

import { registry } from "@web/core/registry"
import { KpiCard } from "./kpi_card/kpi_card"
import { loadJS } from "@web/core/assets"
const { Component, onWillStart, useRef, onMounted } = owl

export class SalesDashboard extends Component {
    setup() {
        onWillStart(async ()=> {
//            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.min.js")
        })
    }
}

SalesDashboard.template = "sales_dashboard.SalesDashboard"
SalesDashboard.components = { KpiCard }
registry.category("actions").add("sales_dashboard", SalesDashboard)