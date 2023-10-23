/* @odoo-module */

import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"
import { loadJS } from "@web/core/assets"
import { getColor } from "@web/views/graph/colors"
import { ChartRenderer } from "./chart_renderer/chart_renderer"

const { Component, onWillStart, useState } = owl

export class InventoryDashboard extends Component {
    // to load the initial datas
    setup() {
        this.orm = useService("orm")
        this.state = useState({
            period: 0,
            type: "incoming_stock",
            chartConfig: {}
        })
        this.domain = [["detailed_type", "=", "product"]]
        onWillStart(async () => {
            await loadJS("/web/static/lib/Chart/Chart.js")
            await this.loadDashboardData()
        })
    }
    // to change the values based on selected period
    async onChangePeriod() {
        await this.loadDashboardData()
    }
    // to change the values based on selected type
    async onChangeType() {
        await this.loadDashboardData()
    }
    // to get product details
    async loadDashboardData() {
        if (this.state.type === "incoming_stock") {
            await this.getStockIncoming()
        } else if (this.state.type === "outgoing_stock") {
            await this.getStockOutgoing()
        }
    }
    // stock incoming values for chart
    async getStockIncoming() {
        this.state.primaryChartTitle = "Incoming Stock"
        const data = await this.orm.call("inventory.dashboard", "get_stock_incoming", [0, this.domain])
        this.env.bus.trigger('renderEvent', {"data": data})
        this.state.chartConfig = {
            type: "bar",
            data: {
                labels: data.products,
                datasets: [{
                    label: "# of Quantity",
                    data: data.incoming_qty,
                    backgroundColor: data.products.map((_, index) => getColor(index)),
                    borderColor: data.products.map((_, index) => getColor(index)),
                    borderWidth: 1,
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            suggestedMin: 0,
                        }
                    }]
                }
            },
        }
    }
    // stock incoming values for chart
    async getStockOutgoing() {
        this.state.primaryChartTitle = "Outgoing Stock"
        const data = await this.orm.call("inventory.dashboard", "get_stock_outgoing", [0, this.domain])
        this.env.bus.trigger('renderEvent', {"data": data})
        this.state.chartConfig = {
            type: "bar",
            data: {
                labels: data.products,
                datasets: [{
                    label: "# of Quantity",
                    data: data.outgoing_qty,
                    backgroundColor: data.products.map((_, index) => getColor(index)),
                    borderColor: data.products.map((_, index) => getColor(index)),
                    borderWidth: 1,
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            suggestedMin: 0,
                        }
                    }]
                }
            },
        }
    }
}

InventoryDashboard.template = "inventory_dashboard.InventoryDashboard"
InventoryDashboard.components = { ChartRenderer }
registry.category("actions").add("inventory_dashboard", InventoryDashboard)
