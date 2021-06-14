# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MyFirstModule(http.Controller):
    # @http.route('/first', auth='public')
    # def index(self, **kw):
    #     return "Hello from my first route"

    
    @http.route('/cars', auth='public', type='http', website=True)
    def display_car(self, **kw):
        cars=request.env["car.car"].search([]).sudo()
        vals={
            'cars': cars
        }
        return request.render('my_first_module.display_cars',vals)


    @http.route('/cars/create', auth='public', type='http', website=True)
    def redirect_to_form_car_create(self, **kw):
        return request.render('my_first_module.create_car_form')

    
    @http.route('/create', auth='public', type='http', website=True)
    def create_new_car(self, **kw):
        name = kw.get("name")
        doors_number = kw.get("doors_number")
        horse_power = kw.get("horse_power")
        
        print("#"*30)
        print("___create_new_car___")
        print("kw",kw)
        print("name:",name)
        print("doors_number:",doors_number)
        print("horse_power:",horse_power)
        print("#"*30)
        
        request.env['car.car'].create({
            'name': name,
            'doors_number': doors_number,
            'horse_power': horse_power,
        })
        
        return request.redirect("/cars")