/* @odoo-module */

import { registry } from "@web/core/registry"

const { Component, useRef, onMounted } = owl

export class ChartRenderer extends Component {
    setup() {
        this.chartRef = useRef("chart")
        this.chart = null
        onMounted(() => {
            this.renderChart()
            this.env.bus.on("renderEvent", this, this.updateChart)
        })
    }
    // to render chart with data from props
    renderChart() {
        this.chart = new Chart(this.chartRef.el , {
            type: this.props.config.type,
            data: this.props.config.data,
            options: this.props.config.options,
        })
    }
    // to update chart with new datas
    updateChart(ev) {
        if (this.chart) {
            const data = ev.data
            console.log(data)
        }
    }
}

ChartRenderer.template = "inventory_dashboard.ChartRenderer"