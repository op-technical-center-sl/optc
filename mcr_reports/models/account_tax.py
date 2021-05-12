from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.tax"

    legal_text = fields.Text("Legal Text")
