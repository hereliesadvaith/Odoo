/** @odoo-module **/

import PaymentScreen from 'point_of_sale.PaymentScreen';
import Registries from 'point_of_sale.Registries';

export const PurchasePaymentScreen = (PaymentScreen) =>
    class extends PaymentScreen {
        async _isOrderValid(isForceValidate) {
            var res = await super._isOrderValid(...arguments)
            if (this.currentOrder.partner) {
                var partner = this.currentOrder.partner
                var payment_lines = this.currentOrder.paymentlines
                var total_amount = 0
                total_amount += partner.total_session_amount
                for (var i=0; i < payment_lines.length ; i++) {
                    var amount = payment_lines[i].amount
                    total_amount += amount
                }
                if (partner.enable_purchase_limit && (partner.purchase_limit_value < total_amount)) {
                    const { confirmed } = await this.showPopup('ErrorPopup', {
                        title: this.env._t('Purchase Limit Reached'),
                        body: this.env._t(partner.name + "'s order is more than purchase limit " + partner.purchase_limit_value),
                    })
                    return false
                } else {
                    partner.total_session_amount += total_amount
                    await this.rpc({
                        model: 'res.partner',
                        method: 'write',
                        args: [[partner.id], { 'total_session_amount': partner.total_session_amount }],
                    })
                    return res
                }
            } else {
                const { confirmed } = await this.showPopup('ConfirmPopup', {
                    title: this.env._t('Customer Required'),
                    body: this.env._t('Please Select a customer to continue.'),
                })
                if (confirmed) {
                    this.selectPartner()
                }
                return false
            }
        }
    }

Registries.Component.extend(PaymentScreen, PurchasePaymentScreen)