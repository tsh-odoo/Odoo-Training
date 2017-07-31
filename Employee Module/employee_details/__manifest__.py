# -*- coding: utf-8 -*-
{
    'name': "employee_details",

    'summary': """the module contains information regarding fresher employee""",

    'description': """
        This Module contains all the information of fresher employee like in which projects they have
        worked on during their studies and their education as well as personal details
    """,

    'author': "Tejas Shahu",
    'website': "http://www.employeedetails.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/assert.xml',
        'views/first_view.xml',
        'views/dashboard.xml',
        'views/templates.xml',
        'views/template_dashboard.xml',
        'report/employee_details_view.xml',
        'report/report_print.xml'
    ],
    'qweb': ['static/src/xml/dashboard.xml'],
    'demo': [
    ],
    # only loaded in demonstration mode
    'aplication': True,
}
