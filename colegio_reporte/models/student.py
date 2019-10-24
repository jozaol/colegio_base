from odoo import fields, api, models

class OpStudentCourse(models.Model):
    _inherit = "op.student.course"    

    @api.onchange('course_id')
    def _compute_subjects(self):
        for rec in self:
            if rec.course_id:
                rec.subject_ids = [[6, 0, rec.course_id.subject_ids.ids]]
