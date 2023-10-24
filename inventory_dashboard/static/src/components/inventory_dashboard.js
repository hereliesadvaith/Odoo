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
            type: "inventory_valuation",
        })
        this.domain = [["detailed_type", "=", "product"]]
        onWillStart(async () => {
            await loadJS("/web/static/lib/Chart/Chart.js")
            await this.loadPrimaryChartData()
            await this.loadWarehouseChartData()
        })
    }
    // to change the values based on selected period
    async onChangePeriod() {
        this.domain = [["detailed_type", "=", "product"]]
        await this.loadPrimaryChartData()
        await this.loadWarehouseChartData()
    }
    // to change the values based on selected type
    async onChangeType() {
        await this.loadPrimaryChartData()
    }
    // to load dashboard data
    async loadPrimaryChartData() {
        if (this.state.type === "incoming_stock") {
            await this.getPrimaryChartData("Incoming Stock", "get_incoming_stock", "# of Quantity")
        } else if (this.state.type === "outgoing_stock") {
            await this.getPrimaryChartData("Outgoing Stock", "get_outgoing_stock", "# of Quantity")
        } else if (this.state.type === "internal_transfer") {
            await this.getPrimaryChartData("Internal Transfer", "get_internal_transfer", "# of Transfers")
        } else if (this.state.type === "average_expense") {
            await this.getPrimaryChartData("Average Expense", "get_average_expense", "$")
        } else if (this.state.type === "inventory_valuation") {
            await this.getPrimaryChartData("Inventory Valuation", "get_inventory_valuation", "$")
        }
    }
    // get data from model functions.
    async getPrimaryChartData(chartTitle, apiMethod, chartLabel) {
        this.state.primaryChartTitle = chartTitle
        const result = await this.orm.call("inventory.dashboard", apiMethod, [0, this.domain])
        this.state.primaryChartConfig = {
            id: "primary_chart",
            data: {
                labels: result.labels,
                datasets: [{
                    label: chartLabel,
                    data: result.data,
                    backgroundColor: result.labels.map((_, index) => getColor(index)),
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
        this.env.bus.trigger('renderEvent', { "config": this.state.primaryChartConfig })
    }
    // get data for warehouse chart
    async loadWarehouseChartData() {
        this.state.warehouseChartTitle = "Warehouse Stock"
        const result = await this.orm.call("inventory.dashboard", "get_stock_location", [0, this.domain])
        const data = {
            labels: ['Category 1', 'Category 2', 'Category 3'],
            datasets: [
                {
                    label: 'Type A',
                    data: [10, 15, 20],
                    backgroundColor: 'rgba(75, 192, 192, 0.5)',
                },
                {
                    label: 'Type B',
                    data: [5, 10, 15],
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                },
            ],
        };
        this.state.warehouseChartConfig = {
            id: "warehouse_chart",
            data: data,
            options: {
                scales: {
                    xAxes: [{
                        stacked: true
                    }],
                    yAxes: [{
                        stacked: true
                    }]
                },
            },
        }
        this.env.bus.trigger('renderEvent', { "config": this.state.warehouseChartConfig })
    }
}

InventoryDashboard.template = "inventory_dashboard.InventoryDashboard"
InventoryDashboard.components = { ChartRenderer }
registry.category("actions").add("inventory_dashboard", InventoryDashboard)
