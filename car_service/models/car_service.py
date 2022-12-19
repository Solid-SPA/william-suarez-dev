# coding: utf-8

from odoo import api, fields, models
from odoo.tools.translate import _

class Service(models.Model):
    _name = 'service'
    _description = 'Service'

    name = fields.Char(string='Service')


class CarService(models.Model):
    _name = 'car.service'
    _description = 'Car Service'

    service_id = fields.Many2one('service', string='Service')
    partner_id = fields.Many2one('res.partner', string='Partner')




