{
    'name': 'Mass Editing Apagen',
    'version': '11.0.1.0.0',
    'author': 'Apagen Solution Pvt. Ltd. ',
    'category': 'Tools',
    'website': 'http://www.apagensolution.com',
    'license': 'GPL-3 or any later version',
    'summary': 'Mass Editing',
    'uninstall_hook': 'uninstall_hook',
    'depends': [
        'base',
    ],
    'data': [
        'views/mass_editing_view.xml',
        'views/template.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
