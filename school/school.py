# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, exceptions, fields, models, _

class School(models.Model):

    _name = 'alumno.school'


    name = fields.Char(string='Nombre', required=True)
    identidad = fields.Char(string='Identidad')

    genero = fields.Selection(string='Género', 
        selection=[('m', 'Másculino'), ('f', 'Feménino'),])
    
    date_birth = fields.Date(string='Fecha de Nacimiento')


    
class SaleOrder(models.Model):
    _inherit = ['sale.order']

   alumno_id = fields.Many2one(comodel_name='alumno.school', string='Alumno')
