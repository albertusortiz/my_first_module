# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

from odoo.addons.portal.controllers.portal import CustomerPortal


class CustomerPortalInherit(CustomerPortal):
    pass


class MyFirstModule(http.Controller):
    @http.route('/ver_productos', auth='public', type='http', website=True)
    def index(self, **kw):
        products=request.env["product.template"].search([]).sudo()
        
        vals={
            'products': products
        }
        
        return request.render('my_first_module.ver_productos', vals)

    
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


    @http.route('/delete', auth='public', type='http', website=True)
    def delete_cars(self, **kw):
        id_car=int(kw.get('id'))

        request.env['car.car'].search([('id','=', id_car)]).unlink()

        return request.redirect('/cars')