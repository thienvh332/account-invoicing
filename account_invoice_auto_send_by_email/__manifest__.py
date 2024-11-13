# Copyright 2023 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    "name": "Account Invoice Auto Send By Email",
    "summary": "Invoice with the email transmit method are send automatically.",
    "version": "18.0.1.0.0",
    "category": "Accounting",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["account", "account_invoice_transmit_method", "edi_account_oca"],
    "website": "https://github.com/OCA/account-invoicing",
    "data": [
        "data/ir_cron.xml",
        "data/edi_configuration.xml",
    ],
    "installable": True,
}
