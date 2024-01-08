# Automated Purchase Order

![Static Badge](https://img.shields.io/badge/Status-In_Production-limegreen)
![Static Badge](https://img.shields.io/badge/Odoo-17.0-violet)


The Automatic Purchase Order module is a custom addition to Odoo that simplifies and automates the creation of purchase orders for products.

## Installation

To install this module in your Odoo instance, follow these steps:

1. Copy the `automated_purchase_order` directory to your Odoo addons directory.
2. Restart your Odoo server.
3. Log in to Odoo as an administrator and enable debug mode.
4. Go to the Apps menu and chose Update Apps List option.
5. Search for 'Automated Purchase Order' and install the module.

## Configuration

After installation, follow these steps to configure and use the module:

1. Enable 'Variants' option in settings and go to the 'Product Variants' page.
2. Open the product for which you want to create purchase order.
3. Click the 'Purchase' button. If the product has vendors and vendor prices set, first vendor details will automatically add to the purchase order wizard.
4. Set the desired reorder quantity and select the preferred vendor.
5. Click 'Confirm'.
