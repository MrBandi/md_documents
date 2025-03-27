{
    'name': 'Markdown Documents',
    'version': '1.0',
    'category': 'Document Management',
    'summary': 'Manage documents in Markdown format',
    'description': """
        This module allows you to create and manage documents in Markdown format.
        Features:
        - Store documents with categories
        - Markdown format support
        - Document read access for non-admin users
    """,
    'author': 'MrBandi',
    'website': 'https://bandi-website.pages.dev',
    'depends': ['base', 'web_editor'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/document_views.xml',
        'views/document_category_views.xml',
        'views/menu_views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'md_documents/static/src/css/markdown_style.css',
        ],
    },
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
