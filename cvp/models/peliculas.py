# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class herencia_contactos(models.Model):
    _inherit="res.partner"
    
    mi_campo_actores=fields.Many2one(
        'cvp.peliculas'
    )
    
# class herencia_productos(models.Model):
#     _inherit="product.template"
    
#     mi_campo_asociado=fields.Many2one(
#         'cvp.peliculas'
#     )

class peliculas(models.Model):
    _name = 'cvp.peliculas'
    _description = 'Modelo para crear películas'

    titulo = fields.Char(
        required=True
    )
    imagen_pelicula = fields.Binary(
        string='Imagen',
        attachment=False,
#         required=True
    )
    fecha_lanzamiento = fields.Date(
        default=fields.Date.today
    )
    longitud_minutos = fields.Integer(
        
    )
    director = fields.Many2one(
        'res.partner',
    )
    actores = fields.One2many(
        'res.partner',
        'mi_campo_actores'
    )
    producto_asociado = fields.Many2one(
        'product.template',
    )
    sinopsis = fields.Text(
        
    )
    genero=fields.Many2many(
        'cvp.generos',
        string="Nombre del genero"
    )
    costo_pelicula = fields.Float(
        
    )
    iva = fields.Float(
        
    )
    total = fields.Float(
        string="Total",
        compute="_calc_total"
    )
    mi_campo_peliculas=fields.Many2one(
        'cvp.studio'
    )
    
    @api.depends('iva')
    def _calc_total(self):
        for record in self:
            record.total = float(record.costo_pelicula) + (float(record.costo_pelicula) * (float(record.iva) / 100))
    

    def comprar_pelicula(self):
        _logger.warning("La pelicula se ha COMPRADO")
#         line_env = self.env['sale.order.line']
#         for wizard in self:
#             for rec in wizard.entries:
#                 new_line = line_env.create({
#                             'product_id': rec.product_id.id,
#                             'name': rec.product_id.name,
#                             'order_id': rec.sale_order_id.id,
#                             'product_uom' : rec.product_id.uom_id.id})                
#                 new_line.product_id_change() #Calling an onchange method to update the record

    def vender_pelicula(self):
        _logger.warning("La pelicula se ha VENDIDO")
#         line_env = self.env['sale.order.line']
#         for wizard in self:
#             for rec in wizard.entries:
#                 new_line = line_env.create({
#                     'titulo': rec.titulo
#                 })                
#                 new_line.product_id_change() #Calling an onchange method to update the record