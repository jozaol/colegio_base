from odoo import models, fields


class OpCourse(models.Model):
    _inherit = 'op.course'
    _description = 'Anyaca plus'

    anyaca_ids=fields.Many2many('colegio.anyaca',string='Año academico')

