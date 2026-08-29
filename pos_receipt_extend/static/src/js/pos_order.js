/** @odoo-module */
import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { patch } from "@web/core/utils/patch";

patch(PosOrder.prototype,{
    get loyaltyPoints(){
        console.log("this is this data",this.priceIncl);
//        console.log("this is loyalty point",this); 245.6555 / 10 = 24.56555
        return Math.round(this.priceIncl/10);
    },
});