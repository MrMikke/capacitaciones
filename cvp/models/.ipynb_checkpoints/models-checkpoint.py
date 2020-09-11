# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cvp(models.Model):
    _name = 'cvp.cvp'
    _description = 'cvp.cvp'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
            

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
    actores=fields.Many2one(
        'res.partner'
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

    