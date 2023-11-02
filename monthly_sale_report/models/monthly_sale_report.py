# -*- coding: utf-8 -*-
from odoo import fields, models
import base64


class MonthlySaleReport(models.Model):
    """
    To create model for sale report
    """
    _name = "monthly.sale.report"
    _description = "Monthly Sale Report"

    name = fields.Char("Name", help="Code for Report")
    partner_ids = fields.Many2many("res.partner", string="Partners")
    team_id = fields.Many2one("crm.team", string="Sales Team")
    period = fields.Selection(selection=[
        ("week", "Weekly"),
        ("month", "Monthly")
    ], required=True)
    start_date = fields.Date("From", help="Set time period")
    end_date = fields.Date("To", help="Set time period")
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("ongoing", "Ongoing"),
            ("paused", "paused")
        ],
        default="draft",
        help="Status of the request"
    )

    # Action Methods

    def action_generate(self):
        """
        To generate sheduled action
        """
        self.state = "ongoing"

    def action_pause(self):
        """
        To pause the sheduled action
        """
        self.state = "paused"

    def cron_monthly_sale_report(self):
        """
        Cron function to send monthly report.
        """
        company_id = self.env.context['allowed_company_ids'][0]
        query = f"""
        SELECT slo.name AS reference, rsp.name AS customer,
        slo.amount_total AS amount, slo.date_order AS date,
        slo.state AS status FROM sale_order AS slo
        INNER JOIN res_partner AS rsp ON
        rsp.id = slo.partner_id
        WHERE slo.company_id = {company_id}
        """
        for record in self.search([("state", "=", "ongoing"),
                                   ("period", "=", "month")]):
            self.env.cr.execute(query)
            sale_orders = self.env.cr.dictfetchall()
            data = {
                "sale_orders": sale_orders,
            }
            sale_report = self.env.ref(
                'monthly_sale_report.pdf_sale_report_action'
            )
            data_record = base64.b64encode(
                self.env['ir.actions.report'].sudo()._render_qweb_pdf(
                    sale_report, [record.id], data=data
                )[0]
            )
            ir_values = {
                'name': 'Sale Report',
                'type': 'binary',
                'datas': data_record,
                'store_fname': data_record,
                'mimetype': 'application/pdf',
                'res_model': 'monthly.sale.report',
            }
            sale_report_attachment_id = self.env[
                'ir.attachment'].sudo().create(
                ir_values)
            if sale_report_attachment_id:
                email_template = self.env.ref(
                    'monthly_sale_report.email_template_sale_report')
                email_template.attachment_ids = [sale_report_attachment_id.id]
                emails = [i.email for i in record.partner_ids]
                if email_template and emails:
                    email_values = {
                        'email_to': emails[0],
                        'email_from': self.env.user.email,
                        'email_cc': emails[1:],
                    }
                    email_template.send_mail(
                        self.id, email_values=email_values, force_send=True)
                    email_template.attachment_ids = [fields.Command.unlink(
                        sale_report_attachment_id.id
                    )]

    def cron_weekly_sale_report(self):
        """
        Cron function to send weekly report.
        """
        company_id = self.env.context['allowed_company_ids'][0]
        query = f"""
        SELECT slo.name AS reference, rsp.name AS customer,
        slo.amount_total AS amount, slo.date_order AS date,
        slo.state AS status FROM sale_order AS slo
        INNER JOIN res_partner AS rsp ON
        rsp.id = slo.partner_id
        WHERE slo.company_id = {company_id}
        """
        for record in self.search([("state", "=", "ongoing"),
                                   ("period", "=", "week")]):
            self.env.cr.execute(query)
            sale_orders = self.env.cr.dictfetchall()
            data = {
                "sale_orders": sale_orders,
            }
            sale_report = self.env.ref(
                'monthly_sale_report.pdf_sale_report_action'
            )
            data_record = base64.b64encode(
                self.env['ir.actions.report'].sudo()._render_qweb_pdf(
                    sale_report, [record.id], data=data
                )[0]
            )
            ir_values = {
                'name': 'Sale Report',
                'type': 'binary',
                'datas': data_record,
                'store_fname': data_record,
                'mimetype': 'application/pdf',
                'res_model': 'monthly.sale.report',
            }
            sale_report_attachment_id = self.env[
                'ir.attachment'].sudo().create(
                ir_values)
            if sale_report_attachment_id:
                email_template = self.env.ref(
                    'monthly_sale_report.email_template_sale_report')
                email_template.attachment_ids = [sale_report_attachment_id.id]
                emails = [i.email for i in record.partner_ids]
                if email_template and emails:
                    email_values = {
                        'email_to': emails[0],
                        'email_from': self.env.user.email,
                        'email_cc': emails[1:],
                    }
                    email_template.send_mail(
                        self.id, email_values=email_values, force_send=True)
                    email_template.attachment_ids = [fields.Command.unlink(
                        sale_report_attachment_id.id
                    )]
