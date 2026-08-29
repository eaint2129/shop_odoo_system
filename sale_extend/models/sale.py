from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_remark = fields.Char('Custom Remark')

    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            if not order.custom_remark:
                continue
            order.picking_ids.write({
                'custom_remark': order.custom_remark,
            })
        return res
