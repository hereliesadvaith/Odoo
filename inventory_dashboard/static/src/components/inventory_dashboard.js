/* @odoo-module */

import { registry } from "@web/core/registry"
import { KpiCard } from "./kpi_card/kpi_card"
import { ChartRenderer } from "./chart_renderer/chart_renderer"
import { ProductTable } from "./product_table/product_table"
import { loadJS } from "@web/core/assets"
import { useService } from "@web/core/utils/hooks"
const { Component, onWillStart, useRef, onMounted, useState } = owl

export class InventoryDashboard extends Component {
    setup() {
        this.orm = useService("orm")
        this.state = useState({
            period: 90,
        })
        onWillStart(async ()=> {
            this.getDates()
            await this.getProductDetails()
        })
    }

    async onChangePeriod() {
        this.getDates()
    }

    getDates(){
        this.state.current_date = moment().subtract(this.state.period, 'days').format('DD/MM/YYYY')
        this.state.previous_date = moment().subtract(this.state.period * 2, 'days').format('DD/MM/YYYY')
    }

    async getProductDetails() {
        const context = {}
        this.product_details = await this.orm.call(
            'inventory.dashboard',
            'get_product_details',
            [0],
            {context: context},
        )
        console.log(this.product_details)
    }

}

InventoryDashboard.template = "inventory_dashboard.InventoryDashboard"
InventoryDashboard.components = { KpiCard, ChartRenderer, ProductTable }
registry.category("actions").add("inventory_dashboard", InventoryDashboard)