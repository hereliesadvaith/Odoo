/** @odoo-module **/

import ClosePosPopup from "point_of_sale.ClosePosPopup"
import  Registries from "point_of_sale.Registries"
var rpc = require('web.rpc')

export const PurchaseClosePosPopup = (ClosePosPopup) =>
    class extends ClosePosPopup {
        async confirm() {
            var res = await super.confirm(...arguments)
            var partners = this.env.pos.partners
            partners.forEach(async (partner) => {
                await rpc.query({
                    model: 'res.partner',
                    method: 'write',
                    args: [[partner.id], { 'total_session_amount': 0 }],
                });
            });
            return res
        }
    }

Registries.Component.extend(ClosePosPopup, PurchaseClosePosPopup)