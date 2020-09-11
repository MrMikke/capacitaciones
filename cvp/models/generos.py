from odoo import models, fields, api

class cvp_peliculas(models.Model):
    _name = 'cvp.generos'
    _description = 'Tabla para generos'
    
    peliculas_generos=fields.Many2many(
        'cvp.peliculas',                              
        string="peliculas"
    )
    nombre=fields.Char(
        string="Nombre"
    )
    descripcion=fields.Text(
        string="descripción"
    )