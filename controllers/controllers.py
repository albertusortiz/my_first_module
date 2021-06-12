# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MyFirstModule(http.Controller):
    @http.route('/first/', auth='public')
    def index(self, **kw):
        print('-----------------First route-----------------')
        return "Hello from my first route"

    
    @http.route('/first/', auth='public')
    def display_car(self, **kw):
        print('-----------------Firt rout-----------------')
        return "Hello from my first route"
