import json
from odoo import http,api,SUPERUSER_ID
from odoo.http import request


class ShopItemAPI(http.Controller):

    @http.route("/shop/api/items",type="http",auth="none",methods=["GET"],csrf=False)
    def get_items(self,**kw):
        env = api.Environment(request.env.cr,SUPERUSER_ID,{})
        items = env["shop.item"].search([],order="id desc")
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

    @http.route("/shop/api/create",type="http",auth="user",methods=["POST"],csrf=False)
    def create_item(self,**kw):
        body= json.loads(request.httprequest.data or "{}")
        item = request.env["shop.item"].create({
                "name":body.get("name"),
                "number":body.get("number"),
                "quantity":body.get("quantity"),
        })
        data = {
            "id":item.id,
            "name":item.name,
        }
        return request.make_response(
            json.dumps({"success":True, "message":"Item created","data":data})
        )
