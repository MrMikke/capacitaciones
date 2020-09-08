# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class libreria(models.Model):
    _name="cyp.libreria"
    _description="Este es el modelo para registrar librerías"
    
    name_libreria=fields.Char(
        string="Nombre",
        required=True
    )
    
    name_encargado=fields.Char(
    )
    
    libros=fields.One2many(
        'cyp.libros',
        'libreria',
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
    
    libreria=fields.Many2one(
        'cyp.libreria',
        string="libreria"
    )
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
    
    def boton_prestamo_true(self):
        _logger.warning("Se presionó True")
        for rec in self:
            rec.disponible_prestamo = True
        
    def boton_prestamo_false(self):
        _logger.warning("Se presionó False")
        for rec in self:
            rec.disponible_prestamo = False
    
    @api.constrains('numero_paginas')
    def _constraint_value(self):
        for rec in self:
            if rec.numero_paginas<=0:
                raise ValidationError("Número de páginas no válido")
    
    @api.depends('numero_paginas')
    def _calc_promedio_hojas(self):
        for record in self:
            record.promedio_paginas = float(record.numero_paginas) / 2
            
class herencia_to_libros(models.Model):
    _inherit="cyp.libros"

    aplicando_herencia=fields.Char(
        string="Aplicando herencia"
    )

class const_wizard_libros(models.TransientModel):
    _name = 'cyp.wizard_libros'
    _description = "Wizard para libros para reportes"
    
    valor_active_id=fields.Char(
        string="Valor del active id"
    )
    
    valor_active_model=fields.Char(
        string="Valor del active model"
    )
    
    libros=fields.Many2many(
        'cyp.libros',
        string="Alumnos"
    )