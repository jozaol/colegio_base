from odoo import fields , models  ,api

class Unidad(models.Model):
    _name = 'colegio.asignaturas'
    _description = 'Asignaturas'

    trimestre_id=fields.Many2one('colegio.trimestre',string='Trimestre',required=True)
    anyaca_id=fields.Many2one('colegio.anyaca',string='Año Académico',required=True)
    unidad_id=fields.Many2one('colegio.unidad',string='Unidad',required=True)
    faculty_id=fields.Many2one('op.faculty',string='Profesor',required=True)
    course_id=fields.Many2one('op.course',string='Course',required=True)
    subject_ids=fields.Many2many('op.subject',string='subject',
                                 compute='_compute_subjects',
                                 inverse='_compute_subjects',
                                 required=True)
    faculty_subject_ids = fields.Many2many('op.subject', string='Subject(s)',
                                           track_visibility='onchange')
                                           
    @api.depends('faculty_id')
    def _compute_subjects(self):
        for rec in self:
            if rec.faculty_id:
                rec.subject_ids = rec.faculty_id.faculty_subject_ids
