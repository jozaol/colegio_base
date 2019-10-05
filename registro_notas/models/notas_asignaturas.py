from odoo import fields , models ,api

class Unidad(models.Model):
    _name = 'colegio.asignaturas'
    _description = 'Asignaturas'

    trimestre_id=fields.Many2one('colegio.trimestre',string='Trimestre')
    anyaca_id=fields.Many2one('colegio.anyaca',string='Año Académico')
    unidad_id=fields.Many2one('colegio.unidad',string='Unidad')
    faculty_id=fields.Many2one('op.faculty',string='Profesor')
    subject_ids=fields.Many2many('op.subject',string='Subject',
                                  )

    @api.onechange('faculty_id')
    def _compute_subjects(self):
        for rec in self:
            if rec.faculty_id:
                rec.subject_ids = [[6, 0, rec.faculty.faculty_subject_ids.id]]

    