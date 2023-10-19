# Survey Contact Creation

![Static Badge](https://img.shields.io/badge/Status-In_Production-limegreen)
![Static Badge](https://img.shields.io/badge/Odoo-16.0-darkviolet)

This Odoo project allows you to automatically create contacts in your database based on the details provided by users when they take a survey. It's a convenient way to manage and collect contact information efficiently.

## Installation

To install this module in your Odoo instance, follow these steps:

1. Copy the `survey_contact_creation` directory to your Odoo addons directory.
2. Restart your Odoo server.
3. Log in to Odoo as an administrator and enable debug mode.
4. Go to the Apps menu and chose Update Apps List option.
5. Search for 'Survey Contact Creation' and click install.

## Configuration

After installation, follow these steps to configure and use the module:

1. While creating/editing the survey, make sure that you have survey questions that collect contact information, such as name, email, phone number, etc.
2. Navigate to 'Contact Relation' page and in questions field you can select the contact information questions and the corresponding partner field for contact model. For example, map the 'Name' question to 'Name' in the contact, 'Email' to 'Email', and so on.
3. Once you've configured the question and field mapping, when a user submits the survey, the system will automatically create a contact record in the `res.partner` model.

