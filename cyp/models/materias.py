# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class materias(models.Model):
    _name="cyp.materias"
    _description="Este es el modelo para registrar materias"
    
    name=fields.Char(
        string="Nombre"
    )
    alumno=fields.Many2one(
        'cyp.alumnos',
        string="Alumnos"
    )
    
class herencia_to_materia(models.Model):
    _inherit="cyp.materias"
    
    nombre2=fields.Char(
        string="Nombre alternativo"
    )
    
class alumnos(models.Model):
    _name="cyp.alumnos"
    _description="ESTE MODELO ES PARA REGISTRAR ALUMNOS"
    
    name=fields.Char(
        String="Nombre del alumno"
    )
    
    recursador=fields.Boolean(
        string="¿Eres recursador?"
    )
    
    def _calc_cyp_materias_count(self):
        for rec in self:
            rec.cyp_materias_count = rec.env['cyp.materias'].search_count([('alumno','=',rec.id)])
    cyp_materias_count = fields.Integer(
        string="Contador de Materias", 
        compute="_calc_cyp_materias_count"
    )
    
    alumnos=fields.One2many(
        'cyp.materias',
        'alumno',
        string="MATERIAS",
#         domain="[('id','!=', '1')]"
    )
    
    alumnos2=fields.Many2one(
        'cyp.materias',
        string="ALUMNOS2"
    )
    alumnos3=fields.Many2many(
        'cyp.materias',
        string="ALUMNOS3"
    )
    
    def boton_consulta(self):
        for rec in self:
            consultas_bd=False
            consultas_bd=rec.env['cyp.alumnos'].search([('name','=','HUGO')])
            for consulta in consultas_bd:
                _logger.warning("ID " + str(consulta.id))
                _logger.warning("NOMBRE " + str(consulta.name))
                for consulta_materias in consulta.alumnos:
                    _logger.warning("ID " + str(consulta_materias.name))

class herencia_visa(models.Model):
    _inherit = "cyp.alumnos"
    _description="Este es un modelo para crear un nuevo formulario y este añadirlo a una vista que ya está hecha aplicando herenncia"
    
    campo_herencia=fields.Char(
        string="Campo de herencia por vista"
    )
            
class cyp_wizard_alumnos(models.TransientModel):
    _name = 'cyp.wizard_alumnos'
    _description = "Wizard para alumnos para reportes"
    
    valor_active_id=fields.Char(
        string="Valor del active id"
    )
    
    valor_active_model=fields.Char(
        string="Valor del active model"
    )
    
    alumnos=fields.Many2many(
        'cyp.alumnos',
        string="Alumnos"
    )
    
    def imprimir(self):
        for rec in self:
            return self.env.ref('cyp.cyp_wizard_alumnos_report').report_action(self)