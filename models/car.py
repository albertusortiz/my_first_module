# -*- coding: utf-8 -*-

from odoo import models, fields


class my_first_module(models.Model):
    _name = 'car.car'
    name=fields.Char(string="Name")
    doors_number=fields.Integer(string="Doors Number")
    horse_power=fields.Integer(string="Horse Power")