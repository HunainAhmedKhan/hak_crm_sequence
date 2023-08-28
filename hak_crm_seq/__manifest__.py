{
    'name': 'CRM Sequence',
    'version': '16.0.1',
    'category': 'crm',
    'summery': 'This app will create a sequence code in crm, while creating new opportunity.',
    'author': 'HAK Technologies',
    'website': "http://www.HAKTechnologies.com",
    'depends': ['base','helpdesk'],

    'data': [
        'views/views.xml',
        'data/ir_sequence_data.xml'
    ],

    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
