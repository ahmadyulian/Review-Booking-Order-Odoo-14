# -*- coding: utf-8 -*-
{
    'name': "review-booking-order-odoo14",

    'summary': """
        Test Ulang Odoo 14""",

    'description': """
       Mengulang kembali test Odoo
    """,

    'author': "Ahmad Yulian",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',
    'application':True,

    # any module necessary for this one to work correctly
    'depends': ['base','sale', 'sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/work_order_views.xml',
        'views/service_team_views.xml',
        'views/booking_order_views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}