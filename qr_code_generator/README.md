# QR Code Generator

![Static Badge](https://img.shields.io/badge/Status-In_Production-limegreen)
![Static Badge](https://img.shields.io/badge/Odoo-16.0-darkviolet)

This Odoo module adds a QR code generator to the system tray, allowing users to input text and generate QR codes that they can download.

## Installation

To install this module in your Odoo instance, follow these steps:

1. Copy the `qr_code_generator` directory to your Odoo addons directory.
2. Restart your Odoo server.
3. Log in to Odoo as an administrator and enable debug mode.
4. Go to the Apps menu and chose Update Apps List option.
5. Search for 'QR Code Generator' and click install.

## Configuration

1. Click on the QR code icon in the system tray to open the QR code generator pop-up.
2. In the pop-up, you will find:
   - A text box to enter the content for the QR code.
   - A 'Generate' button to create the QR code.
   - A 'Download' button to save the generated QR code as an image.
3. Enter the desired text in the text box and click the 'Generate' button.
4. The generated QR code will appear in the pop-up.
5. Click the 'Download' button to save the QR code as an image to your local device.