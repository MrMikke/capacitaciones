# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class cyp(models.Model):
    _name = 'cyp.cyp'
    _description = 'cyp.cyp'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(
        compute="_value_pc",
        store=True
    )
    description = fields.Text()
    
    # @api.onchange('value')
    # def _onchange_value(self):
    #    raise ValidationError("SE REALIZO UN CAMBIO EN EL FIELD VALUE")
    
    @api.constrains('value')
    def _constraint_value(self):
        for rec in self:
            if rec.value==0:
                raise ValidationError("NO PUEDE SER VALOR 0")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
            
    @api.model
    def create(self, values):
        return super(cyp, self).create(values)
    
    def write(self, values):
        _logger.warnig(values)
        return super(cyp, self).write(values)
            
# def herencia_to_cyp(self):
#     _inherit="cyp.cyp"
    
#     nombre_alternativo=fields.Char(
#         string="NOMBRE ALTERNATIVO"
#     )