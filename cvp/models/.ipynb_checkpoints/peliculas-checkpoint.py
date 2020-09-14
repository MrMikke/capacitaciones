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