from odoo import api,fields,models
from odoo.http import request
from odoo.orm.decorators import onchange


class ShopItem(models.Model):
    _name = "shop.item" #model_shop_item or table => shop_item
    _description = "Shop Items"

    name = fields.Char(string='Name')
    number = fields.Integer(string='Item Reference')
    quantity = fields.Float('Stock Quantity')
    is_available = fields.Boolean('Is Available',compute='_compute_available')
    date = fields.Date('Date')
    receive_datetime = fields.Datetime('Receive Datetime')
    state = fields.Selection(selection=[("draft","Draft"),("available","Available"),("sold","Sold")],
                             string="State",
                             default='draft'
                             ) #Draft, Available, Sold
    currency_id = fields.Many2one('res.currency',string="Currency")
    tag_ids = fields.Many2many('shop.item.tag',
                               #relation= 'shop_item_shop_item_tag_rel'
                               string="Tags"
                               )
    # tag_data_ids = fields.Many2many('shop.item.tag',
    #                            relation= 'shop_item_shop_item_tag_test_rel',
    #                            string="Tags"
    #                            )
    item_line_ids = fields.One2many(comodel_name='shop.item.line',inverse_name='item_id',string='Lines')

    @api.depends('quantity')
    def _compute_available(self):
        for rec in self:
            if rec.quantity > 0:
                rec.is_available = True
            else:
                rec.is_available = False

    def action_confirm(self):
        self.state = 'available'


    def action_sold(self):
        self.state = 'sold'


class ShopItemTag(models.Model):
    _name = "shop.item.tag"
    _description = "Shop Item Tag"

    name = fields.Char('Tag Name',required=True)
    color = fields.Integer('Color')


class ShopItemLine(models.Model):
    _name = 'shop.item.line'
    _description = 'Shop Item Line'


    item_id = fields.Many2one('shop.item','Shop Item')
    product_id = fields.Many2one('product.product','Product')
    quantity = fields.Float('Quantity')
    unit_cost = fields.Float('Unit Cost')
    total_amount = fields.Float('Total')

    @api.onchange('quantity','unit_cost')
    def _calculate_total(self):
        # import pdb
        # pdb.set_trace()
        self.total_amount = self.quantity * self.unit_cost
