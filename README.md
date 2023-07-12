# Odoo

Welcome to the Odoo Applications Repository! This repository contains a collection of custom applications developed for Odoo, an open-source enterprise resource planning (ERP) system. Each application within this repository offers specific functionality to enhance and extend the capabilities of Odoo.

Feel free to explore the individual application directories to learn more about each application and how it can benefit your Odoo installation.

## Installation

To install any of the applications included in this repository, please follow these steps:

1. Clone the repository in your Odoo folder.
2. Add the repository path to your addons_path in odoo.conf file.

```
[options]
; Is This The Password That Allows Database Operations:
admin_passwd = admin
db_host = localhost
db_port = 5432
db_user = odoo16
db_password = False
addons_path = /home/user/odoo/addons, /home/user/odoo/our_repository

```
3. Open the Odoo application and go to Apps. From the apps list activate our application.
4. Enable developer mode and from top menu click the Update App List option and enjoy.
