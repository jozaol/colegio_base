from odoo import models, fields,api,_


class OpFacultyCourse(models.Model): 
    _name= "op.faculty.course"
    _description = "Course Plus"
    faculty_course_id=fields.Many2one('op.faculty','Profesor', ondelete="cascade")
    course_id=fields.Many2one('op.course',string='Course')                              
    batch_id=fields.Many2one('op.batch',string='Batch')                   
    subject_ids=fields.Many2many('op.subject',
                                string='subject',
                                )

    @api.onchange('course_id')
    def _compute_batch(self):
        for rec in self:
            if rec.course_id:
                rec.batch_id = [[6,0,rec.course_id.batch_id.id]]
                
class OpSubject(models.Model):
    _inherit = "op.faculty"
    _description = "Batch plus"
    course_detail_ids= fields.One2many('op.faculty.course','faculty_course_id',
                                       'Courses y Batches',
                                       )
    subject_ids = fields.Many2many('op.subject', string='Subject(s)')

    course_id=fields.Many2one('op.course',string='Course')                          
                            

    @api.onchange('course_detail_ids')
    def _compute_subjects(self):
        for rec in self:
            if rec.course_detail_ids:
                rec.faculty_subject_ids = [[6,0,rec.course_detail_ids.course_id.subject_ids.ids]]

