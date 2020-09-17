# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class herencia_contactos(models.Model):
    _inherit="res.partner"
    
    mi_campo_actores=fields.Many2one(
        'cvp.peliculas'
    )
    
# class herencia_productos(models.Model):
#     _inherit="product.template"
    
#     mi_campo_asociado=fields.Many2one(
#         'cvp.peliculas'
#     )

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
    longitud_minutos = fields.Integer(
        
    )
    director = fields.Many2one(
        'res.partner',
    )
    actores = fields.One2many(
        'res.partner',
        'mi_campo_actores'
    )
    producto_asociado = fields.Many2one(
        'product.template',
    )
    sinopsis = fields.Text(
        
    )
    genero=fields.Many2many(
        'cvp.generos',
        string="Nombre del genero"
    )
    costo_pelicula = fields.Float(
        
    )
    iva = fields.Float(
        
    )
    total = fields.Float(
        string="Total",
        compute="_calc_total"
    )
    mi_campo_peliculas=fields.Many2one(
        'cvp.studio'
    )
    
    @api.depends('iva')
    def _calc_total(self):
        for record in self:
            record.total = float(record.costo_pelicula) + (float(record.costo_pelicula) * (float(record.iva) / 100))
    
