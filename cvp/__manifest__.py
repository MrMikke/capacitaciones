# -*- coding: utf-8 -*-
{
    'name': "cvp",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'purchase',
        'sale',
        'sale_management',
        'contacts'
               ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/groups_custom.xml',
        'views/views.xml',
        'views/views_generos.xml',
        'views/views_studio.xml',
        'views/cvp_wizard_peliculas.xml',
        'views/cvp_wizard_generos.xml',
        'views/templates.xml',
        'reports/cvp_peliculas_report.xml',
        'reports/cvp_generos_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
