from odoo import models, fields

class OpFacultyCourse(models.Model):
    _name= "op.faculty.course"
    course_id=fields.Many2one ('op.course','Course',ondelete="cascade",required=True)
    batch_id=fields.Many2one('op.batch','Batch',ondelete="cascade",required=True)