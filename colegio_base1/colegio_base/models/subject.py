from odoo import models, fields


class OpSubject(models.Model):
    _inherit = "op.subject"
    _description = "Subject plus"

    subject_padre_id=fields.Many2one('op.subject','Curso Padre')

