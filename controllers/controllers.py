# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MyFirstModule(http.Controller):
    # @http.route('/first', auth='public')
    # def index(self, **kw):
    #     print('-----------------First route-----------------')
    #     return "Hello from my first route"

    
    @http.route('/cars', auth='public', type='http', website=True)
    def display_car(self, **kw):
        print('-----------------Second route-----------------')
        cars=request.env["car.car"].search([]).sudo()
        vals={
            'cars': cars
        }
        return request.render('my_first_module.display_cars',vals)
