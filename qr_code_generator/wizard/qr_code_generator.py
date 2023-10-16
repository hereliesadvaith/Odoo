# -*- coding: utf-8 -*
from odoo import fields, models
import qrcode
import base64
from io import BytesIO


class QRCodeGenerator(models.TransientModel):
    """
    Model for QR code generator
    """
    _name = "qr.code.generator"
    _description = "QR Code Generator"

    text_box = fields.Char("Text", required=True, help="Text for qr code")
    qr_code = fields.Binary("QR Code", help="QR Code")

    # Action Methods

    def action_generate(self):
        """
        To generate QR Code
        """
        self.ensure_one()
        if qrcode and base64:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=3,
                border=4,
            )
            qr.add_data(self.text_box)
            qr.make(fit=True)
            img = qr.make_image()
            temp = BytesIO()
            img.save(temp, format="PNG")
            qr_image = base64.b64encode(temp.getvalue())
            self.update({
                "qr_code": qr_image,
            })

        return {
            "type": "ir.actions.act_window",
            "name": "QR Code Generator",
            "view_mode": "form",
            "res_model": "qr.code.generator",
            "target": "new",
            "res_id": self.id,
        }

    def action_reset(self):
        """
        To reset the current fields
        """
        return {
            "type": "ir.actions.act_window",
            "name": "QR Code Generator",
            "view_mode": "form",
            "res_model": "qr.code.generator",
            "target": "new",
        }

    def action_download(self):
        """
        To download QR Code image
        """
        self.action_generate()
        return {
            "type": "ir.actions.act_url",
            "target": "self",
            "url": f"/web/image?model=qr.code.generator"
                   f"&download=true&id={self.id}&field=qr_code",
        }
