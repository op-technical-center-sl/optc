from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    code_ice_1 = fields.Char(string="ICE")
    cofor_1 = fields.Char(string="COFOR")
    other_info_1 = fields.Char(string="Other Info Maroc")
    import_information = fields.Char(string="Import Information")

    code_ice = fields.Integer(string="Code ICE")

    show_rex = fields.Boolean(
        string="Show Rex Number",
        help="If checked, REX number is shown in invoices",
    )
