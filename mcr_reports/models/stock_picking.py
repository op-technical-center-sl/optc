from odoo import fields, models, _


class StockPicking(models.Model):
    _inherit = "stock.picking"

    number_of_pallets = fields.Integer(string="Number Of Pallets", copy=False)
    palletized_invoice_id = fields.Many2one(comodel_name="account.move",string="Palletized Invoice")

    def group_products(self): # lines -> stock_move_line
        vals = {}

        # _logger.info("Lines: " + str(lines))
        for line in self.move_line_ids: # lines.product_id['id']:
            if line.product_id in vals.keys():
                vals[line.product_id]["qty"] += line.qty_done
            else:
                vals.update({
                    line.product_id:{
                        'qty':line.qty_done,
                        'move_line': line
                    }})
        # _logger.info("Vals: " + str(vals))
        return vals.items()

        # { move.line(1): qty_done}