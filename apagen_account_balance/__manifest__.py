# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Account Balance',
    'version': '1.1',
    'category': 'Accounting',
    'author': 'Apagen Solutions',
    'website': 'http://www.apagen.com/',
    'license': 'AGPL-3',
    'depends': ['account'],
    'data': [
        'views/account_balance_view.xml',
        'wizard/accnt_balance_check.xml',
    ],

    'demo': [],
    'installable': True,
    'auto_install': False,
    'images': [],
}
