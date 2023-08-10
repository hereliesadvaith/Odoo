import time
import datetime
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.tools import date_utils, float_is_zero
from odoo.exceptions import ValidationError
import io
import json
try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


class ExcelWizard(models.TransientModel):
    _name = "example.xlsx.wizard"
    start_date = fields.Datetime(string="Start Date",
                                 default=time.strftime('%Y-%m-01'),
                                 required=True)
    end_date = fields.Datetime(string="End Date",
                               default=datetime.datetime.now(),
                               required=True)

    def print_xlsx(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start Date must be less than End Date')
        data = {
            'start_date': self.start_date,
            'end_date': self.end_date,
        }
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'example.xlsx.wizard',
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Excel Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        from_date = data['from_date']
        to_date = data['to_date']
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'font_size': '12px', 'align': 'center'})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})
        sheet.merge_range('B2:I3', 'EXCEL REPORT', head)
        sheet.merge_range('A6:B6', 'From Date:', cell_format)
        sheet.merge_range('C6:D6', from_date, txt)
        sheet.write('D6:F6', 'To Date:', cell_format)
        sheet.merge_range('G6:H6', to_date, txt)
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
