# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class generos(models.Model):
    _name = 'cvp.generos'
    _description = 'Modelo para crear generos de películas'

    genero=fields.Many2many(
        'cvp.peliculas',
        string="Nombre del genero"
    )
#     descripcion=fields.Many2many(
#         'cyp.peliculas',
#         string="Descripción"
#     )

    alumnos3=fields.Many2many(
            string="ALUMNOS3"
        )