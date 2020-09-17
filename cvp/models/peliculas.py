# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime
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

    name = fields.Char(
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
        'product.product',
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
    
    state = fields.Selection(
        [
            ('A','Activa'),
            ('I','Inactiva'),
        ], 
        string="Estatus", 
        default='A'
    )
    
    def activate(self):
        for rec in self:
            rec.state="A"
    
    def inactive(self):
        for rec in self:
            rec.state="I"
    
    @api.depends('iva')
    def _calc_total(self):
        for record in self:
            record.total = float(record.costo_pelicula) + (float(record.costo_pelicula) * (float(record.iva) / 100))

    def vender_pelicula(self):
        for rec in self:
            _logger.warning("La pelicula se ha VENDIDO")
            sale_order = self.env['sale.order'].create({
                "partner_id": rec.env.user.id,
                "date_order": datetime.datetime.now(),
            })
            detalle = self.env['sale.order.line'].create({
                "order_id": sale_order.id,
                "product_id": rec.producto_asociado.id,
                "name": rec.producto_asociado.name,
                "product_uom_qty": 1,
                "product_uom": rec.producto_asociado.uom_id.id,
                "price_unit": rec.total,
            })
        
            
    def comprar_pelicula(self):
        for rec in self:
            _logger.warning("La pelicula se ha COMPRADO")
            purchase_order = self.env['purchase.order'].create({
                    "partner_id": rec.env.user.id,
                    "date_order": datetime.datetime.now(),
            })
            detalle = self.env['purchase.order.line'].create({
                "order_id": purchase_order.id,
                "product_id": rec.producto_asociado.id,
                "name": rec.producto_asociado.name,
                "product_qty": 1,
                "product_uom": rec.producto_asociado.uom_id.id,
                "price_unit": rec.total,
                "date_planned": datetime.datetime.now()
            })