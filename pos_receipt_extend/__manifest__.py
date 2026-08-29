{
    "name":"POS Receipt Extend",
    "version":"19.0.1.0.1",
    "category":"POS",
    "summary":"Extend sales order",
    "depends":['point_of_sale'],
    "assets":{
        "point_of_sale._assets_pos":[
            "pos_receipt_extend/static/src/js/pos_order.js",
            "pos_receipt_extend/static/src/js/payment_screen.js",
            "pos_receipt_extend/static/src/xml/pos_receipt.xml",
        ],
    },
    "installable":True,
    "application":False,
    "license": "LGPL-3",
}