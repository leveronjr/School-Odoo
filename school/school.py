# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class School (models.Model):
	_name = 'school.schol'
	nombreAlumno = fields.Char(string='nombre_completo',requiered=True)
	edad = fields.Integer(string="edad",requiered=True)
	sexo = fields.Char(string="sexo",requiered=True)
	encargado = fields.Char(string="encargado")
	fecha_matricula = fields.Date(string='fecha_matricula')