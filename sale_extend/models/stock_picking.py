from odoo import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    custom_remark = fields.Char('Custom Remark')
