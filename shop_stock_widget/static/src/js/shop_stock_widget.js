/** @odoo-module */
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class StockStockWidget extends Component {
    static template = "shop_stock_widget.ShopStockWidget";
    static props = {
        ...standardFieldProps,
    };

    get quantity(){
        return Number(this.props.record.data[this.props.name] || 0); //25.4 => 25
    }

    get statusClass(){
        if(this.quantity <= 0){
            return "empty";
        } else if(this.quantity < 10){
            return "low";
        }else{
            return "ready";
        }
    }
    get statusLabel(){
        if(this.quantity <= 0){
            return "No Stock";
        } else if(this.quantity < 10){
            return "Low Stock";
        }else{
            return "In Stock";
        }
    }
    get progressWidth(){
        const percent = Math.min(Math.max(this.quantity,0),100);
        return `${percent}%`; //percent = 50, 40 50% ${percent} => 50 + % => 50%,
    }
    onQuantityInput(ev) {
        const value = Number(ev.target.value || 0);
        this.props.record.update({[this.props.name]:value});
    }
}

export const shopStockWidget = {
    component: StockStockWidget,
    supportedTypes: ["float","integer"],
};

registry.category("fields").add("shop_stock_badge",shopStockWidget);