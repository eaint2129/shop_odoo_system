import json
from odoo import http
from odoo.http import request

class ShopItemAPI(http.Controller):

    @http.route("/shop/api/items",type="http",auth="none",methods=["GET"],csrf=False)
    def get_items(self,**kw):
        items = request.env["shop.item"].search([],order="id desc")
        data = []
        for item in items:
            data.append({
                "id":item.id,
                "name":item.name,
                "sequence":item.sequence,
                "qty":item.quantity,
                "state":item.state,
            })
        return request.make_response(
            json.dumps({
                "success":True,
                "data":data
            }),headers=[("Content-Type","application/json")],
        )