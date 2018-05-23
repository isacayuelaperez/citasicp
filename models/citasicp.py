# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class citasicp(models.Model): 
    _name = 'ej.citasicp' 
    Autor = fields.Char(string='Autor', required=True) 
 
    Cita = fields.Text(string='Cita', required=True) 
 
    Fecha_validacion = fields.Datetime(string='Fecha_validacion', required=True) 
 
    Orden_validacion = fields.Integer(string='Orden_validacion', required=True) 
 
