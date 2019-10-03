from odoo import models, fields

class OpSubject(models.Model):
    _inherit = "op.faculty"
    _description = "Batch plus"
    course_detail_ids= fields.One2many('op.faculty.course','course_id',
                                       'Courses y Batches')