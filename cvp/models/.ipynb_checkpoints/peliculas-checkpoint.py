# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class peliculas(models.Model):
    _name = 'cvp.peliculas'
    _description = 'Modelo para crear películas'

    titulo = fields.Char(
        required=True
    )
    imagen_pelicula = fields.Binary(
        string='Imagen',
        attachment=False,
#         required=True
    )
    fecha_lanzamiento = fields.Date(
        default=fields.Date.today
    )
    fecha_actual = fields.Date(
        default=fields.Date.today,
        readonly=True
    )
    longitud_minutos = fields.Float(
        
    )
    director = fields.Char(
        
    )
    actores = fields.Char(
        
    )
    producto_asociado = fields.Char(
        
    )
    sinopsis = fields.Char(
        
    )
    costo_pelicula = fields.Float(
        
    )
    iva = fields.Float(
        
    )
    total = fields.Float(
        
    )
    
    @api.onchange('fecha_lanzamiento')
    def _onchange_fecha_lanzamiento(self):
        for rec in self:
            _logger.warning("-- Fecha actual actual --")
            _logger.warning(rec.fecha_actual.day)
#             _logger.warning(rec.fecha_lanzamiento.month)
            
#     @api.constrains('fecha_lanzamiento')
#     def _constraint_fecha_lanzamiento(self):
#         for rec in self:
#             if rec.value==0:
#                 raise ValidationError("NO PUEDE SER VALOR 0")