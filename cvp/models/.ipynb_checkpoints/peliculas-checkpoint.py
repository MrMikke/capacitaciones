# -*- coding: utf-8 -*-

from odoo import models, fields, api


class peliculas(models.Model):
    _name = 'cvp.peliculas'
    _description = 'Modelo para crear películas'

    imagen_pelicula = fields.Binary(
        string='Imagen película',
        attachment=False
    )