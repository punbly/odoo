# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Real Estate Management',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'sequence': 15,
    'summary': 'Track leads and close opportunities',
    'website': 'https://www.odoo.com/app',
    'depends': [
        'base_setup',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/real_estate_property.xml',

        'views/menu.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
