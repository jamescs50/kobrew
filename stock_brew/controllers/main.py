from odoo import http


class Beverages(http.Controller):
    @http.route('/drinks', auth='public')
    def list(self, **kwargs):
        drink = http.request.env['stock.beverage']
        drinks = drink.search([])
        return http.request.render('')
