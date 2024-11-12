# Copyright 2023 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import _, api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def cron_send_email_invoice(self):
        invoices = self.search(self._email_invoice_to_send_domain())
        for invoice in invoices:
            self._event("on_send_via_email_account").notify(invoice)

    def _execute_invoice_sent_wizard(self, options=None):
        self.ensure_one()
        if self.is_move_sent:
            return _("This invoice has already been sent.")
        res = self.action_invoice_sent()
        wiz_ctx = res["context"] or {}
        wiz_ctx["active_model"] = self._name
        wiz_ctx["active_ids"] = self.ids
        wiz = self.env["account.move.send.wizard"].with_context(**wiz_ctx).create({})
        return wiz.action_send_and_print()

    @api.model
    def _email_invoice_to_send_domain(self):
        return [
            ("move_type", "in", ("out_invoice", "out_refund")),
            ("state", "=", "posted"),
            ("is_move_sent", "=", False),
            ("transmit_method_code", "=", "mail"),
            ("payment_state", "=", "not_paid"),
        ]
