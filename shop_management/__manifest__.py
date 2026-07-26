{
    "name":"Shop Management",
    "version":"19.0.1.0.1",
    "category":"Sales",
    "summary":"Simple shop course example for junior odoo developer.",
    "depends":['product'],
    "data":[
        'security/ir.model.access.csv',
        'views/shop_item_views.xml',
        'views/shop_menu_views.xml'
    ],
    "installable":True,
    "application":True,
    "license": "LGPL-3",
}