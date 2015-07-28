# -*- coding: utf-8 -*-
{
    'name': "mrc_payment_charge",

    'summary': """
        addebito spese di vendita al cliente""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Marco Longo",
    'website': "https://it.linkedin.com/pub/marco-longo/31/958/424",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/payment.xml',
        'views/invoice.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
