# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class generos(models.Model):
    _name = 'cvp.generos'
    _description = 'Modelo para crear generos de películas'
    
    genero=fields.Char(
        string="Nombre del genero"
    )
    
    descripcion=fields.Text(
        string="Descripción del genero"
    )

    peliculas=fields.Many2many(
        'cvp.peliculas',
        string="Nombre del genero"
    )
    
    def _calc_cvp_peliculas_count(self):
        for rec in self:
            rec.cvp_peliculas_count = rec.env['cvp.peliculas'].search_count([('genero','=',rec.id)])
    cvp_peliculas_count = fields.Integer(
        string="Contador de peliculas", 
        compute="_calc_cvp_peliculas_count"
    )
#     descripcion=fields.Many2many(
#         'cvp.peliculas',
#         string="Descripción"
#     )

#     alumnos3=fields.Many2many(
#             string="ALUMNOS3"
#         )