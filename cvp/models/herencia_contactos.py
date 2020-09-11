# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cvp_herencia_contactos(models.Model):
    _inherit = 'res.partner'
    
    director=fields.Many2one(
        'cvp.peliculas',
        string="Director"
    )
