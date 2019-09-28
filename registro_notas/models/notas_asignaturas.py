from odoo import fields , models  

class Unidad(models.Model):
    _name = 'colegio.asignaturas'
    _description = 'Asignaturas'

    trimestre_id=fields.Many2one('colegio.trimestre',string='Trimestre',required=True)
    anyaca_id=fields.Many2one('colegio.anyaca',string='Año Académico',required=True)
    unidad_id=fields.Many2one('colegio.unidad',string='Unidad',required=True)
    faculty_id=fields.Many2one('op.faculty',string='Profesor',required=True)
    subject_id=fields.Many2one('op.subject',string='Asignatura',required=True)