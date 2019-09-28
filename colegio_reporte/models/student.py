from odoo import fields, api, models

class OpStudentCourse(models.Model):
    _inherit = "op.student.course"

    subject_ids = fields.Many2many(compute='_compute_subjects', inverse='_compute_subjects', store=True)
    

    @api.depends('course_id')
    def _compute_subjects(self):
        for rec in self:
            if rec.course_id:
                rec.subject_ids = rec.course_id.subject_ids