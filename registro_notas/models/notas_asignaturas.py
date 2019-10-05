from odoo import fields , models  ,api

class Unidad(models.Model):
    _name = 'colegio.asignaturas'
    _description = 'Asignaturas'

    trimestre_id=fields.Many2one('colegio.trimestre',string='Trimestre')
    anyaca_id=fields.Many2one('colegio.anyaca',string='Año Académico')
    unidad_id=fields.Many2one('colegio.unidad',string='Unidad')
    faculty_id=fields.Many2one('op.faculty',string='Profesor')
# subject_ids=fields.Many2many('op.subject',
#                               string='Subject',
#                                compute='_compute_subjects',
#                                inverse='_compute_subjects',
#                                store=True)
#
#    @api.depends('faculty_id')
#    def _compute_subjects(self):
#        for rec in self:
#            if rec.faculty_id:
#*                rec.subject_ids = rec.faculty_id.faculty_subject_ids 