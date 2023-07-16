# -*- coding: utf-8 -*-
{
    'name': "ucloud",

    'summary': """
        """,

    'description': """
        
    """,

    'author': "Yoshi",
    'website': "https://www.ucloud.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets':{
        'web.assets_backend':[
            'ucloud/static/src/js/config.js'
        ]
    },
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'sequence': 0,
}
