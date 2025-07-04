# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Airline Database',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Manage Airline Data',
    'website': 'https://www.odoo.com/app',
    'depends': [
        'base_setup',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/airline_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
