/* @odoo-module */

import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"
import { ChartRenderer } from "./chart_renderer/chart_renderer"

const { Component, onWillStart, useState } = owl

export class InventoryDashboard extends Component {
    // to load the initial datas
    setup() {
        this.orm = useService("orm")
        this.state = useState({
            period: 0,
            type: "inventory_valuation"

        })
        onWillStart(async () => {
            this.getDates()
            await this.loadDashboardData()
        })
    }
    // to get dates in database format
    getDates() {
        this.state.current_date = moment().subtract(this.state.period, 'days').format('DD/MM/YYYY')
    }
    // to change the values based on selected period
    async onChangePeriod() {
        this.getDates()
        console.log(this.state.period)
    }
    // to change the values based on selected type
    async onChangeType() {
        this.getDates()
        console.log(this.state.type)
    }
    // to get product details
    async loadDashboardData() {
        const products = await this.orm.searchRead("product.product", [], [])
        console.log(products)
    }
}

InventoryDashboard.template = "inventory_dashboard.InventoryDashboard"
InventoryDashboard.components = { ChartRenderer }
registry.category("actions").add("inventory_dashboard", InventoryDashboard)
