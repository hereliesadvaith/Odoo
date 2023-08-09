from odoo import models, api


class WarrantyReport(models.AbstractModel):
    """Abstract model for our warranty report"""
    _name = 'report.warranty.report_warranty'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env["warranty.report.wizard"].browse(docids)
        res = {
            'doc_ids': docids,
            'doc_model': 'warranty.report.wizard',
            'docs': docs,
            'data': data,
        }
        return res
