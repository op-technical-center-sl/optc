from odoo import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    report_secondary_logo = fields.Image(string="Secondary Logo (on reports)", attachment=True)

    rex_number = fields.Char(string="Rex Number")
