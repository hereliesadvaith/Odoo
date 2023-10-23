/* @odoo-module */

import { registry } from "@web/core/registry"

const { Component, useRef, onMounted } = owl

export class ChartRenderer extends Component {
    setup() {
        this.chartRef = useRef("chart")
        onMounted(() => this.renderChart())
    }

    renderChart() {
        new Chart(this.chartRef.el , {
            type: this.props.config.type,
            data: this.props.config.data,
            options: this.props.config.options,
        })
    }
}

ChartRenderer.template = "inventory_dashboard.ChartRenderer"