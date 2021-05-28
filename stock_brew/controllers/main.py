from odoo import http


class Beverages(http.Controller):
    @http.route('/drinks', auth='public')
    def list(self, **kwargs):
        drink = http.request.env['stock.beverage']
        drinks = drink.sudo().search([])
        return http.request.render('stock_brew.drink_list_template', {'drinks': drinks})
