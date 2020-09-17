# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class studio(models.Model):
    _name = 'cvp.studio'
    _description = 'Modelo para crear studios'
    
    nombre_studio=fields.Char(
        string="Nombre del genero"
    )
    
    peliculas=fields.One2many(
        'cvp.peliculas',
        'mi_campo_peliculas',
    )
    
#     descripcion=fields.Many2many(
#         'cyp.peliculas',
#         string="Descripción"
#     )

#     alumnos3=fields.Many2many(
#             string="ALUMNOS3"
#         )