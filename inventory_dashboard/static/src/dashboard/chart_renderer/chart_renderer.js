/* @odoo-module */

import { registry } from "@web/core/registry"

const { Component, useRef, onMounted } = owl

export class ChartRenderer extends Component {
    setup() {
        this.chartRef = useRef("chart")
        this.charts = {}
        onMounted(() => {
            this.renderChart()
            this.env.bus.on("renderEvent", this, this.updateChart)
        })
    }
    // to render chart with data from props
    renderChart() {
        this.charts[this.props.config.id] = new Chart(this.chartRef.el, {
            type: this.props.type,
            data: this.props.config.data,
            options: this.props.config.options,
        })
    }
    // to update chart with new datas
    updateChart(ev) {
        if (this.charts[ev.config.id]) {
            this.charts[ev.config.id].data = ev.config.data
            this.charts[ev.config.id].update()
        }
    }
}

ChartRenderer.template = "inventory_dashboard.ChartRenderer"