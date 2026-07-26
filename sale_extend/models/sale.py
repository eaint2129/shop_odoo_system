from odoo import fields,models,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_remark = fields.Char('Custom Remark')