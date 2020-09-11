# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cvp_herencia_contactos(models.Model):
    _inherit = 'res.partner'
    
    actores=fields.Many2one(
        'cvp.peliculas',
        string="Actores"
    )
