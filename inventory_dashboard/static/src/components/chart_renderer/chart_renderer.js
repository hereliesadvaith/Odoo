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
        this.chart = new Chart(this.chartRef.el, {
            type: this.props.config.type,
            data: this.props.config.data,
            options: this.props.config.options,
        })
    }
    // to update chart with new datas
    updateChart(ev) {
        if (this.chart) {
            const config = ev.config
            this.chart.type = config.type
            this.chart.data = config.data
            this.chart.options = config.options
            this.chart.update()
        }
    }
}

ChartRenderer.template = "inventory_dashboard.ChartRenderer"