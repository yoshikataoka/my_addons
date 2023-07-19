# -*- coding: utf-8 -*-
{
    'name': "Auto Call Center",

    'summary': """
        """,

    'description': """
        
    """,

    'author': "Yoshi",
    'website': "",


    'category': 'Uncategorized',
    'version': '0.1',


    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_company.xml',
    ],
    "assets": {
        'web._assets_primary_variables': [
            'call_center/static/src/css/colors.scss',
        ],
    },
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'sequence': 0,
}
