# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class cyp(models.Model):
    _name = 'cyp.cyp'
    _description = 'cyp.cyp'

    name = fields.Char(
        string="Nombre desde el modelo"
    )
    value = fields.Integer()
    value2 = fields.Float(
        compute="_value_pc", 
        store=True
    )
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
            
    @api.constrains('value')
    def _check_value(self):
        for rec in self:
            if rec.value==0:
                raise ValidationError("Value no puede ser 0")

class cyp_triangulo(models.Model):
    _name = 'cyp.triangulos'
    _description="Modelo para calcular el triangulo"
    
    base=fields.Float(
        string="base"
    )
    
    total=fields.Float(
        string="total"
    )
    
class cyp_triangulo_altura(models.Model):
    _inherit="cyp.triangulos"
    
    altura=fields.Float(
        string="Altura"
    )
    