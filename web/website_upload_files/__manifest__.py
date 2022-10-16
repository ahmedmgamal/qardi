
{
    'name': 'Website File Upload',
    'version': '14.0.1.0.0',
    'summary': 'Option To Upload Files In Website',
    'description': 'Option To Upload Files In Website',
    'author': 'my company',
    'license': 'LGPL-3',
    'depends': [
        'website_sale',
        'sale_management',
    ],
    'data': [
        'views/website_sale_templates.xml',
        'views/sale_order_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'assets': {
            'web.assets_frontend': [
                'website_upload_files/static/src/js/attachment.js',
            ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
