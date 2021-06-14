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

        request.env['car.car'].create({
            'name': name,
            'doors_number': doors_number,
            'horse_power': horse_power,
        })
        
        return request.redirect("/cars")

    
    @http.route('/update', auth='public', type='http', website=True)
    def redirect_to_form_update(self, **kw):
        id_car=int(kw.get('id'))
        print('car id =',id_car)
        vals={}
        car_object=request.env['car.car'].search([('id','=', id_car)])
        vals.update({
            'car':car_object
        })
        return request.render("my_first_module.update_car_form",vals)

    
    @http.route('/update/car', auth='public', type='http', website=True)
    def update_car(self, **kw):

        id_car = int(kw.get("id"))
        name = kw.get("name")
        doors_number = kw.get("doors_number")
        horse_power = kw.get("horse_power")

        request.env['car.car'].search([('id','=',id_car)]).write({
            'name': name,
            'doors_number': doors_number,
            'horse_power': horse_power,
        })

        return request.redirect('/cars')