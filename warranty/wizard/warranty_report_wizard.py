# -*- coding: utf-8 -*-
from odoo import models, fields
from odoo.exceptions import ValidationError, MissingError


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

    def action_confirm(self):
        """
        To print the pdf report the report
        """
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError("Set valid period")
        query = """
        select pro.id, rfw.name as warranty, rfw.state, res.name as partner,
        rfw.request_date, ptm.name as product
        from request_for_warranty as rfw
        inner join product_product as pro
        on rfw.product_id = pro.id
        inner join product_template as ptm
        on pro.product_tmpl_id = ptm.id
        inner join res_partner as res
        on rfw.customer_id = res.id
        where rfw.id > 0
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
            products = tuple(i.id for i in self.product_ids)
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
