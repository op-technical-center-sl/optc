{
    "name": "MCR Reports Customization",
    "summary": " MCR Reports Customization and Customization of OPTC workflow",
    "category": "",
    "version": "13.0.1.0.1",
    "author": "Odoo PS, MCR solutions International (Vicent Cubells)",
    "website": "http://www.odoo.com, https://int.mcr-solutions.com/",
    "license": "OEEL-1",
    "depends": [
        'web',
        'account',
        'sale',
        'sale_management',
        'sale_stock',
        'stock',
        'contacts'
    ],
    "data": [
        "views/account_move_views.xml",
        "views/res_partner_views.xml",
        "views/res_company_views.xml",
        "views/stock_picking_views.xml",
        "views/account_tax_views.xml",
        # "views/sale_order_views.xml",
        # "views/product_pricelist_view.xml",
        "views/report/account_report_invoice_document.xml",
        "views/report/stock_report_delivery_document.xml",
        "views/report/report_saleorder_document.xml",
        "views/report/report_purchaseorder_document.xml",
        "views/report/web_external_layout.xml",
        "data/report_documents.xml",
    ],
    "css": [
        "static/src/css/web_external_layout.css"
    ],
    "task_id": [2464205, 2484801],
}
