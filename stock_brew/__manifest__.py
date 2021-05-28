{
    'name':'Brewing',
    'description': 'record information about the brewed products and brewing process',
    'author': 'James Carr-Saunders',
    'depends': ['base','product','stock'],
    'application': False,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'security/stock_beverage_security.xml',
        'views/beverage_views.xml',
        'views/brewing_menus.xml',
        'views/product_views.xml',
        'views/drink_list_template.xml',
    ],
}
