# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, exceptions, fields, models

class School(models.Model):

    _name = 'alumno.school'
    name = fields.Char(string='Nombre', required=True)
    edad = fields.Integer(string='Edad')
    genero = fields.Selection(string='Género', 
        selection=[('m', 'Másculino'), ('f', 'Feménino'),])
    date_birth = fields.Date(string='Fecha de Nacimiento')
