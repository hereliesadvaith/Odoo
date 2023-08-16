# -*- coding: utf-8 -*-
import io
import json
import xlsxwriter
from odoo import models, fields
from odoo.exceptions import ValidationError, MissingError
from odoo.tools import date_utils


class WarrantyReportWizard(models.TransientModel):
    """
    Model for wizard
    """
    _name = "warranty.report.wizard"
    _description = "Warranty Report Wizard"

    product_ids = fields.Many2many("product.product",
                                   string="Product",
                                   help="Product")
    partner_id = fields.Many2one("res.partner")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    # Action methods

    def print_pdf(self):
        """
        To print the pdf report the report
        """
        company_id = self.env.context['allowed_company_ids'][0]
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError("Set valid period")
        query = f"""
        select pro.id, rfw.name as warranty, rfw.state, res.name as partner,
        rfw.request_date, ptm.name as product
        from request_for_warranty as rfw
        inner join product_product as pro
        on rfw.product_id = pro.id
        inner join product_template as ptm
        on pro.product_tmpl_id = ptm.id
        inner join res_partner as res
        on rfw.customer_id = res.id
        where rfw.company_id = {company_id}
        """
        products = False
        partner = False
        unique_products = []
        if self.start_date:
            query += f"""
           and rfw.request_date >= '{self.start_date}' """
        if self.end_date:
            query += f"""
            and rfw.request_date <= '{self.end_date}' """
        if self.product_ids:
            products = tuple(self.product_ids.ids)
            if len(products) > 1:
                query += f"""
                and rfw.product_id in {products}"""
            else:
                query += f"""
                and rfw.product_id = {self.product_ids.id}"""
            products = True
        if self.partner_id:
            query += f"""
                and rfw.customer_id = {self.partner_id.id}"""
            partner = True
        self.env.cr.execute(query)
        warranties = self.env.cr.dictfetchall()
        for warranty in warranties:
            warranty['state'] = warranty['state'].replace("_", " ").title()
        if len(warranties) == 0:
            raise MissingError("No records found")
        if self.product_ids:
            product_list = [
                [i['id'], i['product']['en_US']] for i in warranties]
            for i in product_list:
                if i not in unique_products:
                    unique_products.append(i)
        data = {
            'warranties': warranties,
            'products': products,
            'partner': partner,
            'unique_products': unique_products,
        }
        return self.env.ref('warranty.warranty_report_action').report_action(
            None, data=data)

    def print_xlsx(self):
        """
            To print the xlsx report the report
        """
        company_id = self.env.context['allowed_company_ids'][0]
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError("Set valid period")
        print(self.env["request.for.warranty"].sudo().search([]))
        query = f"""
                select pro.id, rfw.name as warranty, rfw.state,
                res.name as partner, rfw.request_date, ptm.name as product
                from request_for_warranty as rfw
                inner join product_product as pro
                on rfw.product_id = pro.id
                inner join product_template as ptm
                on pro.product_tmpl_id = ptm.id
                inner join res_partner as res
                on rfw.customer_id = res.id
                where rfw.company_id = {company_id}
                """
        products = False
        partner = False
        unique_products = []
        if self.start_date:
            query += f"""
                   and rfw.request_date >= '{self.start_date}' """
        if self.end_date:
            query += f"""
                    and rfw.request_date <= '{self.end_date}' """
        if self.product_ids:
            products = tuple(self.product_ids.ids)
            if len(products) > 1:
                query += f"""
                        and rfw.product_id in {products}"""
            else:
                query += f"""
                        and rfw.product_id = {self.product_ids.id}"""
            products = True
        if self.partner_id:
            query += f"""
                        and rfw.customer_id = {self.partner_id.id}"""
            partner = True
        self.env.cr.execute(query)
        warranties = self.env.cr.dictfetchall()
        for warranty in warranties:
            warranty['state'] = warranty['state'].replace("_", " ").title()
        if len(warranties) == 0:
            raise MissingError("No records found")
        if self.product_ids:
            product_list = [
                [i['id'], i['product']['en_US']] for i in warranties]
            for i in product_list:
                if i not in unique_products:
                    unique_products.append(i)
        data = {
            'warranties': warranties,
            'products': products,
            'partner': partner,
            'unique_products': unique_products,
            'start_date': self.start_date,
            'end_date': self.end_date
        }
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'warranty.report.wizard',
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Excel Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        """
        To generate xlsx report
        """
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        sheet.set_column('A:F', 20)
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        sheet.merge_range('A1:F2', 'WARRANTY REPORT', head)
        data_list = []
        index = 6
        if data['partner']:
            sheet.write('A4', 'Customer')
            sheet.write('B4', data['warranties'][0]['partner'])
            for warranty in data['warranties']:
                data_list.append(
                    [warranty['warranty'],
                     warranty['product']['en_US'],
                     warranty['state'],
                     warranty['request_date']])
                index += 1
            sheet.add_table(f"A6:D{index}",
                            {"data": data_list,
                                "columns": [{'header': 'Warranty'},
                                            {'header': 'Product'},
                                            {'header': 'State'},
                                            {'header': 'Request Date'}]})
        else:
            for warranty in data['warranties']:
                data_list.append(
                    [warranty['warranty'],
                     warranty['partner'],
                     warranty['product']['en_US'],
                     warranty['state'],
                     warranty['request_date']])
                index += 1
            sheet.add_table(f"A6:E{index}",
                            {"data": data_list,
                                "columns": [{'header': 'Warranty'},
                                            {'header': 'Customer'},
                                            {'header': 'Product'},
                                            {'header': 'State'},
                                            {'header': 'Request Date'}]})
        if data['start_date']:
            sheet.write('A3', 'Date From')
            sheet.write('B3', data['start_date'])
            if data['end_date']:
                sheet.write('D3', 'Date To')
                sheet.write('E3', data['end_date'])
        elif data['end_date']:
            sheet.write('A3', 'Date To')
            sheet.write('B3', data['end_date'])
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
