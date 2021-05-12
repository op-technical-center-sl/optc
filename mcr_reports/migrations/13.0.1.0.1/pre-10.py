import logging
import os

from odoo import SUPERUSER_ID, api
from odoo.addons.mcr_reports.migrations import util

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})

    if "ODOO_STAGE" in os.environ and os.environ['ODOO_STAGE'] == "dev":
        _logger.info('Exit migration script : dev env database !')
        return ""

    

    _logger.info('###################################################################################')
    _logger.info('Begin pre_10')

    _logger.info('----------RENAME MODELS----------')
    to_rename_models = ()

    for model in to_rename_models:
        cr.execute("UPDATE ir_model SET state='base' WHERE model LIKE '%s'" % model[0])
        util.rename_model(cr, model[0], model[1], rename_table=model[2])
        _logger.info('rename model : %s -> %s' % (model[0], model[1]))

    _logger.info('----------RENAME FIELDS----------')

    to_rename_fields = (
                       ('res.partner', 'x_studio_ice', 'code_ice'),
                       ('res.partner', 'x_studio_ice_1', 'code_ice_1'),
                       ('res.partner', 'x_studio_cofor_1', 'cofor_1'),
                       ('res.partner', 'x_studio_other_info_1', 'other_info_1'),
                       ('res.partner', 'x_studio_import_information', 'import_information'),
                       ('account.move', 'x_studio_import_information', 'import_information'),
                       ('account.move', 'x_studio_information_programme', 'information_program'),
                       ('account.move', 'x_studio_type_of_invoice', 'invoice_type'),
                       ('account.move', 'x_studio_total_delivery_weight', 'total_delivery_weight'),
                       ('account.move', 'x_studio_shipping_number_1', 'shipping_number_1'),
                       ('account.move', 'x_studio_number_of_palets', 'number_of_pallets'),
    )

    for field in to_rename_fields:
        cr.execute("UPDATE ir_model_fields SET state='base' WHERE name LIKE '%s' AND model LIKE '%s'" % (field[1], field[0]))
        util.rename_field(cr, field[0], field[1], field[2])
        _logger.info('rename field : %s -> %s on model %s' % (field[1], field[2], field[0]))

    _logger.info('----------REMOVE VIEWS----------')

    to_remove_views = [
        "studio_customization.odoo_studio_account__5fe4ba78-e8db-4a47-a558-21d0e8f3e55c",
        "studio_customization.odoo_studio_res_part_45e9e17a-dd63-47b0-89d7-8a2250bc4220",
        "studio_customization.odoo_studio_report_d_4367b6a8-cdeb-4813-bb8a-eb917c5293ae",
        "studio_customization.odoo_studio_report_i_bd0991d6-79d6-4f70-8eed-01d666179340"
    ]

    for view in to_remove_views:
        util.remove_view(cr, xml_id=view)
