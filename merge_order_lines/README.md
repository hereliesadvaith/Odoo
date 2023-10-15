# Merge Order Lines

![Static Badge](https://img.shields.io/badge/Status-In_Production-limegreen)
![Static Badge](https://img.shields.io/badge/Odoo-16.0-darkviolet)


This module is an extension for Odoo that simplifies the management of sales orders by automatically merging order lines with same product and unit price. This feature helps streamline your order entry process and maintain cleaner, more organized sales orders.

## Installation

To install this module in your Odoo instance, follow these steps:

1. Copy the `merge_order_lines` directory to your Odoo addons directory.
2. Restart your Odoo server.
3. Log in to Odoo as an administrator and enable debug mode.
4. Go to the Apps menu and chose Update Apps List option.
5. Search for 'Merge Order Lines' and click install.

## Configuration

When this module is installed, any time you save a sales order, the module will automatically merge order lines with the same product and unit price.