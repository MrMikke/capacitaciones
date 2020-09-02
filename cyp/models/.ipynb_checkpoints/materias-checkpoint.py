# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class materias(models.Model):
    _name="cyp.materias"
    _description="Este es el modelo para registrar materias"
    
    name=fields.Char(
        string="Nombre"
    )