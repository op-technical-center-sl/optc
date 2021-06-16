from odoo import api, models, fields



class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def _prepare_invoice(self):
        values = super()._prepare_invoice()
        #aqui viene la personalización
        values.update({
            'number_of_pallets': sum(self.picking_ids.mapped('number_of_pallets'))
        })
        return values


class AccountMove(models.Model):
    _inherit = "account.move"

    import_information = fields.Char(string="Import Information")
    information_program = fields.Char(string="Information Program")
    shipping_number_1 = fields.Char(string="Shipping Number")

    total_delivery_weight = fields.Float(string="Total Delivery Weight")

    # number_of_pallets = fields.Integer(string="Number of Pallets", compute="_compute_number_of_pallets", store=True)
    number_of_pallets = fields.Integer(string="Number of Pallets")
    # calc_number_of_pallets = fields.Integer(related='number_of_pallets', compute="_compute_number_of_pallets", store=True)

    picking_ids = fields.One2many(related="invoice_line_ids.sale_line_ids.order_id.picking_ids")

    invoice_type = fields.Selection(string="Type of Invoice", selection=[
        ('Producción', 'Production'),
        ('I+D', 'I+D'),
        ('Servicios', 'Services'),
        ('Inversiones', 'Investments'),
        ('Gastos', 'Expenses'),
    ])

    legal_text = fields.Char(string="Legal Text", compute="_compute_legal_text")

    @api.depends("invoice_line_ids.tax_ids")
    def _compute_legal_text(self):
        for invoice in self:
            legal_text = invoice.mapped("invoice_line_ids.tax_ids.legal_text")
            invoice.legal_text = ", ".join([lt for lt in legal_text if type(lt) == str])

    @api.depends(
        "picking_ids",
        "picking_ids.number_of_pallets",
        "picking_ids.state",
        "picking_ids.palletized_invoice_id",
        "picking_ids.move_lines.returned_move_ids.state"
    )
    def _compute_number_of_pallets(self):
        for invoice in self:
            # Filter to get pickings that are or can be linked to this invoice
            pickings = invoice.picking_ids.filtered(
                lambda x: x.state == "done" and
                x.picking_type_code == "outgoing" and
                (not x.palletized_invoice_id or x.palletized_invoice_id == self) and
                not x.move_lines.returned_move_ids.filtered(lambda y: y.state == "done")
            )
            pickings.write({"palletized_invoice_id": invoice.id})
            invoice.number_of_pallets = sum(pickings.mapped("number_of_pallets"))

