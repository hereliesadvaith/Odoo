/** @odoo-module **/

import PaymentScreen from 'point_of_sale.PaymentScreen';
import Registries from 'point_of_sale.Registries';

export const PurchasePaymentScreen = (PaymentScreen) =>
    class extends PaymentScreen {
        setup () {
            super.setup()
        }
        async _isOrderValid(isForceValidate) {
            var res = await super._isOrderValid(...arguments)
            if (this.currentOrder.partner) {
                var partner = this.currentOrder.partner
                var payment_lines = this.currentOrder.paymentlines
                var total_amount = 0
                for (var i=0; i < payment_lines.length ; i++) {
                    var amount = payment_lines[i].amount
                    total_amount += amount
                }
                if (partner.enable_purchase_limit && (partner.purchase_limit_value < total_amount)) {
                    const { confirmed } = await this.showPopup('ErrorPopup', {
                        title: this.env._t('Purchase Limit Reached'),
                        body: _.str.sprintf(this.env._t(partner.name + "'s order is more than purchase limit " + partner.purchase_limit_value)),
                    })
                    return false
                } else {
                    return res
                }
            } else {
                const { confirmed } = await this.showPopup('ConfirmPopup', {
                    title: this.env._t('Customer Required'),
                    body: _.str.sprintf(this.env._t('Please Select a customer to continue.')),
                })
                if (confirmed) {
                    this.selectPartner()
                }
                return false
            }
        }
    }

Registries.Component.extend(PaymentScreen, PurchasePaymentScreen)