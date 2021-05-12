from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    number_of_pallets = fields.Integer(string="Number Of Pallets", copy=False)
    palletized_invoice_id = fields.Many2one(comodel_name="account.move",string="Palletized Invoice")
