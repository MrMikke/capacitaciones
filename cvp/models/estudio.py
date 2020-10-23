from odoo import models, fields, api
from odoo.exceptions import ValidationError

class studio(models.Model):
    _name = 'cvp.studio'
    _description = 'Modelo para crear studios'
    
    name=fields.Char(
        string="Nombre del genero"
    )
    
    peliculas=fields.One2many(
        'cvp.peliculas',
        'mi_campo_peliculas',
    )