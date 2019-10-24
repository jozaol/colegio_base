from odoo import fields , models ,api

class Unidad(models.Model):
    _name = 'colegio.asignaturas'
    _description = 'Asignaturas'

    trimestre_id=fields.Many2one('colegio.trimestre',string='Trimestre')
    anyaca_id=fields.Many2one('colegio.anyaca',string='Año Académico')
    unidad_id=fields.Many2one('colegio.unidad',string='Unidad')
    faculty_id=fields.Many2one('op.faculty',string='Profesor')
<<<<<<< HEAD
    subject_ids=fields.Many2one('op.subject',string='Subject',)
    batch_id=fields.Many2one('op.batch',string='Batch')
    student_notas_ids=fields.One2many('colegio.notas_alumno','student_id',string='Notas Mensuales')



















## Este api permite que automaticamente todos los curso del profesor al ser seleccionado aparescan inmediatamente
##    @api.onchange("faculty_id")
##    def _compute_subjects(self):
##        for rec in self:
##            if rec.faculty_id:
##                rec.subject_ids = [[6,0,rec.faculty_id.faculty_subject_ids.id]]

=======
    # subject_ids=fields.Many2many('op.subject',string='Subject',
    #                               )

    # @api.onechange('faculty_id')
    # def _compute_subjects(self):
    #     for rec in self:
    #         if rec.faculty_id:
    #             rec.subject_ids = [[6, 0, rec.faculty.faculty_subject_ids.id]]
>>>>>>> 6f61f4ba5cbe124c428a3731831481986035a204

    