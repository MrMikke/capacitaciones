# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
import datetime
import pytz
_logger = logging.getLogger(__name__)

class cvp_peliculas(models.Model):
    _name = 'cvp.peliculas'
    _description = 'Tabla para peliculas'
    
    current_user = fields.Many2one('res.users','Current User', default=lambda self: self.env.user)
    #CAMPO USADO PARA HACER EL STATUSBAR
    state = fields.Selection(
        [
            ('A','Activa'),
            ('I','Inactiva'),
        ], 
        string="Estatus", 
        default='A'
    )
    imagen_pelicula=fields.Binary(
        string="Portada",
        required=True
    )
    name=fields.Char(
        string="Descripción"
    )
    fecha_lanzamiento=fields.Date(
        string="Fecha de lanzamiento"
    )
    longitud_minutos=fields.Float(
        string="Duración en minutos"
    )
    producto_asociado=fields.Many2one(
        'product.product',
        string="Producto"
    )
    actores_contactos=fields.One2many(
        'res.partner',
        'actores',
        string="Actores"
    )
    studio=fields.Many2one(
        'cvp.studios',
        string="Estudio"
    )
    director=fields.Many2one(
        'res.partner',
        string="Director"
    )
    generos=fields.Many2many(
        'cvp.generos',
        string="Generos"
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
    @api.depends('costo_pelicula','iva')
    def _calc_total(self):
        for rec in self:
            rec.total=rec.costo_pelicula+(rec.costo_pelicula*(rec.iva/100))
    total=fields.Float(
        string="Total del costo",
        compute="_calc_total"
    )
    
    @api.constrains('iva')
    def _check_iva(self):
        for rec in self:
            if rec.iva<0 and rec.iva>100:
                raise ValidationError("El iva no puede ser menor a 0% ni mayor a 100%")
                
    
    def activate(self):
        for rec in self:
            rec.state="A"
    
    def inactive(self):
        for rec in self:
            rec.state="I"
            
    def create_sale(self):
        for rec in self:
            _logger.warning("CREAR VENTA")
            sale_order = rec.env['sale.order'].create({
                "partner_id": rec.current_user.id,
                "date_order": datetime.datetime.now(),
            })
            detalle=rec.env['sale.order.line'].create({
                "order_id": sale_order.id,
                "product_id":  rec.producto_asociado.id,
                "name":  rec.producto_asociado.name,
                "product_uom_qty": 1,
                "product_uom": rec.producto_asociado.uom_id.id,
                "price_unit": rec.total,
            
            })
            
            
    
    
    def create_purchase(self):
        for rec in self:
            _logger.warning("CREAR COMPRA")
            purchase_order = rec.env['purchase.order'].create({
                "partner_id": rec.current_user.id,
                "date_order": datetime.datetime.now(),
            })
            detalle=rec.env['purchase.order.line'].create({
                "order_id": purchase_order.id,
                "product_id":  rec.producto_asociado.id,
                "name":  rec.producto_asociado.name,
                "product_qty": 1,
                "product_uom": rec.producto_asociado.uom_id.id,
                "price_unit": rec.total,
                "date_planned": datetime.datetime.now(),
            })
            
            


    