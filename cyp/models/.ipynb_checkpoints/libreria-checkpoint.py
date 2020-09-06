# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class libreria(models.Model):
    _name="cyp.libreria"
    _description="Este es el modelo para registrar librerías"
    
    name_libreria=fields.Char(
        required=True
    )
    
    name_encargado=fields.Char(
    )
    
    libros=fields.One2many(
        'cyp.libros',
        'name_libro',
        string="Libros"
    )
    
    @api.model
    def create(self, values):
        _logger.warning("Se imprimió desde el Create")
        return super(libreria, self).create(values)
    
    def write(self, values):
        _logger.warning("Se imprimió desde el Edit")
        return super(libreria, self).write(values)
    
class libros(models.Model):
    _name="cyp.libros"
    _description="ESTE MODELO ES PARA REGISTRAR LIBROS"
    
    name_libro=fields.Char(
        String="Nombre del libro"
    )
    
    name_autor=fields.Char(
        String="Nombre del autor"
    )
    
    numero_paginas=fields.Integer(
        string="numero de paginas",
        default=2
    )
    
    promedio_paginas=fields.Float(
        string="promedio",
        compute="_calc_promedio_hojas"
    )
    
    disponible_prestamo=fields.Boolean(
        string="¿Está disponible para préstamo?"
    )
    
#     def herencia_to_cyp(self):
#     _inherit="cyp.cyp"
    
#     nombre_alternativo=fields.Char(
#         string="NOMBRE ALTERNATIVO"
#     )
    
    @api.constrains('numero_paginas')
    def _constraint_value(self):
        for rec in self:
            if rec.numero_paginas<=0:
                raise ValidationError("Número de páginas no válido")
    
    @api.depends('numero_paginas')
    def _calc_promedio_hojas(self):
        _logger.warning("Ejecutó _calc_promedio_hojas")
        for record in self:
            record.promedio_paginas = float(record.numero_paginas) / 2