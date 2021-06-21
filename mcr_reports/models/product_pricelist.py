from odoo import api, models, fields, _
import logging

_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
    _inherit='sale.order.line'

    # programmeLine = fields.Char(string="Programme", related='product_id.pricelist_id.item_ids.programme', \
    #  domain=[('product_id.pricelist_id','=','pricelist_id'), ('product_id', '=', 'order_line.product_id')], readonly=True)
    # programmeLine = fields.Float(string="Programme", related='product_id.qty_available', readonly=True)
    #domain=[('product_id.pricelist_id','=','pricelist_id')]
    #related='product_id.pricelist_id.item_ids.programme')

    # programmeLine = fields.Char(string="Programme")

    programmeLine = fields.Char(string="Programme", compute='_compute_programme')

    def _compute_programme(self):
        for record in self:
            order_id = record.order_id
            tarifa_id = record.order_id.pricelist_id
            product_id = record.product_id
            # _logger.info("Tarifa: " + str(tarifa_id))
            # _logger.info("Pedido: " + str(order_id))
            # _logger.info("Producto: " + str(product_id.id))
            product_tmpl_id = self.env['product.product'].search([('id', '=', product_id.id)])
            # _logger.info("Producto Template: " + str(product_tmpl_id.product_tmpl_id))
            producto_en_tarifa = self.env['product.pricelist.item'].search([('product_tmpl_id', '=', product_tmpl_id.product_tmpl_id.id), ('pricelist_id', '=', tarifa_id.id)])

            # _logger.info("Producto en tarifa: " + str(producto_en_tarifa))
            # _logger.info("Programme en tarifa: " + str(producto_en_tarifa.programme))
            # programme_code = self.env['product.pricelist.item.pr']
            # programme_code = self.env['']
            # programme_code = self.env['sale.order'].search([('pricelist_id', '=', self.order_id.pricelist_id)])
            # #programme_code = self.env['sale.order'].search([('pricelist_id', '=', self.order_id.pricelist_id)])
            record.programmeLine = producto_en_tarifa.programme




class PriceListItems(models.Model):
    _inherit='product.pricelist.item'

    programme = fields.Char(String="Programme")