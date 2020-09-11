# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class cvp_peliculas(models.Model):
    _name = 'cvp.peliculas'
    _description = 'Tabla para peliculas'

    imagen_pelicula=fields.Binary(
        string="Portada",
        required=True
    )
    titulo=fields.Char(
        string="Descripción"
    )
    fecha_lanzamiento=fields.Date(
        string="Fecha de lanzamiento"
    )
    longitud_minutos=fields.Float(
        string="Duración en minutos"
    )
    producto_asociado=fields.Many2one(
        'product.template',
        string="Producto"
    )
    actores_contactos=fields.One2many(
        'res.partner',
        'actores',
        string="Actores"
    )
    studio=fields.Many2one(
        'cvp.studios',
        string="Estudio"
    )
    director=fields.Many2one(
        'res.partner',
        string="Director"
    )
    
    sinopsis=fields.Text(
        string="Sinopsis"
    )
    costo_pelicula=fields.Float(
        string="Costo pelicula"
    )
    iva=fields.Float(
        string="Iva"
    )
    @api.depends('costo_pelicula','iva')
    def _calc_total(self):
        for rec in self:
            rec.total=rec.costo_pelicula+(rec.costo_pelicula*(rec.iva/100))
    total=fields.Float(
        string="Total del costo",
        compute="_calc_total"
    )
    
    @api.constrains('iva')
    def _check_iva(self):
        for rec in self:
            if rec.iva<0 and rec.iva>100:
                raise ValidationError("El iva no puede ser menor a 0% ni mayor a 100%")
    
            

    