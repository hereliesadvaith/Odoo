# Odoo

Welcome to the Odoo Applications Repository! This repository contains a collection of custom applications developed for Odoo, an open-source enterprise resource planning (ERP) system. Each application within this repository offers specific functionality to enhance and extend the capabilities of Odoo.

Please explore the individual application directories inside git branches to learn more about each application and how it can benefit your Odoo installation.

## Installation

To install any of the applications included in this repository, please follow these steps:

1. Clone the repository in your Odoo folder.

-> For Odoo 16

```
git clone https://github.com/hereliesadvaith/Odoo --depth 1 --branch 16.0 ./custom_modules
```

-> For Odoo 17

```
git clone https://github.com/hereliesadvaith/Odoo --depth 1 --branch 17.0 ./custom_modules
```

2. Add the repository path to your addons_path in odoo.conf file.

```
[options]
; This password is used as master password in odoo.
admin_passwd = admin
db_host = localhost
db_port = 5432
db_user = username
db_password = password
addons_path = /home/user/odoo/addons, /home/user/odoo/custom_modules

```
3. Open the Odoo application and go to Apps. From the apps list activate our application.
4. Enable developer mode and from top menu click the Update App List option.

**Important Notice**: Please note that some of the apps included in this repository may be in the development stage marked with ![Static Badge](https://img.shields.io/badge/Status-In_Development-orange) . We strongly recommend using only the applications marked with ![Static Badge](https://img.shields.io/badge/Status-In_Production-limegreen) in a live production environment. Apps in the development stage may not be fully stable or feature-complete and are primarily intended for testing and development purposes.

Enjoy the enhanced features and functionalities these production-ready applications bring to your Odoo ERP system!
