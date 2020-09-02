# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class cyp(models.Model):
    _name = 'cyp.cyp'
    _description = 'Asasdasdsa'

    name = fields.Char()
    value = fields.Integer()
    
    value2 = fields.Float(
        compute="_value_pc", 
        store=True
    )
    alumnos=fields.Many2one(
        'cyp.alumnos',
        string="Alumno"
    )
    alumno_id=fields.Integer(
        string="ID DEL ALUMNO",
        related="alumnos.id"
    )
    
    description = fields.Text()
    
#     @api.onchange('value','name')
#     def _onchange_value(self):
#         raise ValidationError("SE REALIZO UN CAMBIO EN EL FIELD VALUE")
    
    
    @api.constrains('value')
    def _constraint_value(self):
        for rec in self:
            if rec.value==0:
                raise ValidationError("NO PUEDE SER EL VALUE 0")
                
    
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
            
    @api.model
    def create(self, values):
        return super(cyp, self).create(values)
    
    def write(self,values):
        _logger.warning(values)
        return super(cyp, self).write(values) 

    