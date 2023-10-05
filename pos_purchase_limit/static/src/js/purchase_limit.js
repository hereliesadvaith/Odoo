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
                for (var i=0; i < payment_lines.length ; i++) {
                    if (payment_lines[i].name == "Customer Account") {
                        var amount = payment_lines[i].amount
                        partner.balance_due += amount
                        var credit_limit = this.currentOrder.pos.config.due_limit_value
                        if (partner.balance_due > credit_limit) {
                            const { confirmed } = await this.showPopup('ErrorPopup', {
                                title: this.env._t('Due Limit Reached'),
                                body: _.str.sprintf(this.env._t('Customer due is reached ' + credit_limit)),
                            })
                            return false
                        } else {
                            await this.rpc({
                                model: 'res.partner',
                                method: 'write',
                                args: [[partner.id], { 'balance_due': partner.balance_due }],
                            })
                        }
                    }
                }
            } else {
                const { confirmed } = await this.showPopup('ErrorPopup', {
                    title: this.env._t('Customer Required'),
                    body: _.str.sprintf(this.env._t('Please Select a customer')),
                })
                return false
            }
            return res
        }
    }

Registries.Component.extend(PaymentScreen, PurchasePaymentScreen)