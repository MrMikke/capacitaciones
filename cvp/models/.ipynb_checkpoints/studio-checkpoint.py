from odoo import models, fields, api

class cvp_studios(models.Model):
    _name = 'cvp.studios'
    _description = 'Tabla para estudios'
    
    pelicula_studio=fields.One2many(
        'cvp.peliculas',
        'studio',
        string="Peliculas"
    )
    name=fields.Char(
        string="Nombre"
    )
    descripcion=fields.Text(
        string="Descripción"
    )
    
    