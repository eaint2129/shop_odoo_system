{
    "name":"Shop Stock Widget",
    "version":"19.0.1.0.0",
    "category":"Sales",
    "summary":"Custom Widget",
    "depends":['shop_management'],
    "data":[
        'views/shop_item_views.xml',
    ],
    "assets":{
       "web.assets_backend":[
            "shop_stock_widget/static/src/js/shop_stock_widget.js",
            "shop_stock_widget/static/src/scss/shop_stock_widget.scss",
            "shop_stock_widget/static/src/xml/shop_stock_widget.xml",
       ],
    },
    "installable":True,
    "application":False,
    "license": "LGPL-3",
}