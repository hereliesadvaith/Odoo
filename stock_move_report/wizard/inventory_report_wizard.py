# -*- coding: utf-8 -*
from odoo import fields, models
from odoo.exceptions import ValidationError, MissingError


class InventoryReportWizard(models.TransientModel):
    """
    Model for inventory report wizard
    """
    _name = "inventory.report.wizard"
    _description = "Inventory Report Wizard"

    product_ids = fields.Many2many("product.product", string="Products",
                                 help="Select Products")
    picking_type_ids = fields.Many2many("stock.picking.type", string="Transfer Type",
                                    help="Select Locations")
    state = fields.Selection(selection=[
            ("draft", "Draft"),
            ("waiting", "Waiting Another Operation"),
            ("confirmed", "Waiting"),
            ("assigned", "Ready"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
        ],
        help="Status", string="Status")
    start_date = fields.Date(string="Start Date", help="Start Date")
    end_date = fields.Date(string="End Date", help="End Date")

    # Action Methods

    def print_pdf(self):
        """
        To print pdf report
        """
        company_id = self.env.context['allowed_company_ids'][0]
        if self.start_date and self.end_date:
            if self.start_date >= self.end_date:
                raise ValidationError("Set valid period")
        query = f"""
        SELECT stm.date, stm.reference, ptm.name AS product,
        stl.complete_name AS from, std.complete_name AS to,
        stm.product_uom_qty AS quantity, stm.state AS status,
        spt.name AS picking_type
        FROM stock_move AS stm
        INNER JOIN product_product AS ppr
        ON stm.product_id = ppr.id
        INNER JOIN product_template AS ptm
        ON ppr.product_tmpl_id = ptm.id
        INNER JOIN stock_location as stl
        ON stm.location_id = stl.id
        INNER JOIN stock_location as std
        ON stm.location_dest_id = std.id
        INNER JOIN stock_picking as spk
        ON stm.picking_id = spk.id
        INNER JOIN stock_picking_type as spt
        ON spk.picking_type_id = spt.id
        WHERE stm.company_id = {company_id}
        """
        if self.start_date:
            query += f"""
           and stm.date >= '{self.start_date}' """
        if self.end_date:
            query += f"""
            and stm.date <= '{self.end_date}' """
        if self.product_ids:
            products = tuple(self.product_ids.ids)
            if len(products) > 1:
                query += f"""
                and stm.product_id in {products}"""
            else:
                query += f"""
                and stm.product_id = {self.product_ids.id}"""
        if self.picking_type_ids:
            picking_types = tuple(self.picking_type_ids.ids)
            if len(picking_types) > 1:
                query += f"""
                and spk.picking_type_id in {picking_types}"""
            else:
                query += f"""
                and spk.picking_type_id = {self.picking_type_ids.id}"""
        if self.state:
            query += f"""
                and stm.state = '{self.state}'
            """
        query += "ORDER BY stm.date DESC"
        self.env.cr.execute(query)
        stock_moves = self.env.cr.dictfetchall()
        unique_picking_types = list(set([i['picking_type']['en_US'] for i in stock_moves]))
        if len(stock_moves) == 0:
            raise MissingError("No records found")
        for move in stock_moves:
            move['status'] = move['status'].title()
        data = {
            "stock_moves": stock_moves,
            "unique_picking_types": unique_picking_types,
        }
        return self.env.ref("stock_move_report.inventory_report_action").report_action(
            None, data=data
        )

    def print_xlsx(self):
        """
        To print xlsx report
        """
        print("hi there")