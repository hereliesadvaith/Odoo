# Restrict Payment Acquirer

![Static Badge](https://img.shields.io/badge/Status-In_Production-limegreen)
![Static Badge](https://img.shields.io/badge/Odoo-16.0-darkviolet)

This Odoo module allows you to restrict payment providers based on minimum and maximum transaction amounts set for each provider. This is useful for scenarios where you want to limit certain payment methods based on the transaction amount.

## Installation

To install this module in your Odoo instance, follow these steps:

1. Copy the `restrict_payment_acquirer` directory to your Odoo addons directory.
2. Restart your Odoo server.
3. Log in to Odoo as an administrator and enable debug mode.
4. Go to the Apps menu and chose Update Apps List option.
5. Search for 'Restrict Payment Acquirer' and click install.

## Configuration

After installation, follow these steps to configure and use the module:

1. In 'Payment Providers' go to configuration page.
2. You can set the minimum and maximum amount under configuration page.
3. After configuring the minimum and maximum amounts for your payment providers, transactions will be restricted based on these settings.
4. If a transaction amount falls outside the specified range, the payment provider will not be available for the customer to select during checkout.