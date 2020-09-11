# -*- coding: utf-8 -*-

from odoo import models, fields, api



class cvp_peliculas(models.Model):
    _name = 'cvp.peliculas'
    _description = 'Tabla para peliculas'

    imagen_pelicula=fields.Binary(
        string="Portada"
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
    contacto_director=fields.One2many(
        'res.partner',
        'director',
        string="Director"
    )
    actores=fields.Many2one(
        'res.partner',
        string="Actores"
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
    total=fields.Float(
        string="Total del costo"
    )

    