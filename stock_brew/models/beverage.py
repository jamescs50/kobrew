from odoo import fields, models, api


class StockBeverage(models.Model):
    _name = 'stock.beverage'
    _description = 'Beverage'

    name = fields.Char('Name', index=True, required=True)
    taste_note = fields.Html('Tasting Notes')
    active = fields.Boolean("Active", default=True)
    company_id = fields.Many2one('res.company', string='Company', readonly=True, index=True)

    image = fields.Binary('Logo', max_width=128, max_height=128)
