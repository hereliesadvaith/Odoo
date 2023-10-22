/* @odoo-module */

import { loadJS } from "@web/core/assets"

const { Component, onWillStart, useRef, onMounted } = owl

export class ChartRenderer extends Component {
    // to load the initial datas
    setup() {
        this.chartRef = useRef("chart")
        onWillStart(() => loadJS("/web/static/lib/Chart/Chart.js"))
        onMounted(() => this.renderChart())
    }
    // to render chart with passing data.
    renderChart() {
        var xyValues = [
            { x: 50, y: 7 },
            { x: 60, y: 8 },
        ]
        new Chart(this.chartRef.el, {
            type: this.props.type,
            data: {
                datasets: [{
                    pointRadius: 4,
                    pointBackgroundColor: "rgb(0,0,255)",
                    data: xyValues
                }]
            },
            options: {
                legend: { display: false },
                scales: {
                    xAxes: [{ ticks: { min: 40, max: 160 } }],
                    yAxes: [{ ticks: { min: 6, max: 16 } }],
                },
                title: {
                    display: true,
                    text: this.props.title,
                    position: 'bottom'
                }
            },
        })
    }
}

ChartRenderer.template = "inventory_dashboard.ChartRenderer"
