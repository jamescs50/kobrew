from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    beverage_id = fields.Many2one('stock.beverage', string='Beverage')
