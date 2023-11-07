/**@odoo-module **/

import { PosGlobalState } from 'point_of_sale.models'
import Registries from 'point_of_sale.Registries'

const NewPosGlobalState = (PosGlobalState) => class NewPosGlobalState extends PosGlobalState {
    async _processData(loadedData) {
        await super._processData(...arguments)
        this.combo_product = loadedData['combo.product']
    }
    // _save_to_server(orders, options) {
    //     var result = super._save_to_server(orders, options)
    //     return result
    // }
}
Registries.Model.extend(PosGlobalState, NewPosGlobalState)
