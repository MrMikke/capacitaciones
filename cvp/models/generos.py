# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class generos(models.Model):
    _name = 'cvp.generos'
    _description = 'Modelo para crear generos de películas'
    
    name=fields.Char(
        string="Nombre del genero"
    )
    
    descripcion=fields.Text(
        string="Descripción del genero"
    )

    peliculas=fields.Many2many(
        'cvp.peliculas',
        string="Nombre de la película"
    )
    
    def _calc_cvp_peliculas_count(self):
        for rec in self:
            rec.cvp_peliculas_count = rec.env['cvp.peliculas'].search_count([('genero','=',rec.id)])
    cvp_peliculas_count = fields.Integer(
        string="Contador de peliculas", 
        compute="_calc_cvp_peliculas_count"
    )
    
class cvp_wizard_generos(models.TransientModel):
    _name = 'cvp.wizard_generos'
    _description = "Wizard para generos para reportes"
    
    valor_active_id=fields.Char(
        string="Valor del active id",
    )
    
    valor_active_model=fields.Char(
        string="Valor del active model"
    )
    
    name=fields.Char(
        string="Nombre del genero"
    )
    
    solo_generos=fields.Boolean(
        default=True
    )
    
    peliculas=fields.Many2many(
        'cvp.peliculas',
    )
    
    todos_los_generos=fields.Many2many(
        'cvp.generos',
    )
    
    @api.onchange('valor_active_id')
    def _onchange_active_id(self):
        _logger.warning("ON CHANGE")
        for rec in self:
            genero_record=rec.env['cvp.generos'].search([('id','=',rec.valor_active_id)])
            rec.name=genero_record.name
            for peliculas in genero_record.peliculas:
                rec.peliculas+=peliculas
            
            _logger.warning("-------------")
#             _logger.warning("genero_record.genero: " + genero_record.genero)
            for ciclo in genero_record.name:
                _logger.warning("ciclo_a: " + ciclo)
                
    def imprimir(self):
            return self.env.ref('cvp.cvp_wizard_generos_report').report_action(self)