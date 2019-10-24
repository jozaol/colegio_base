from odoo import models, fields


class OpCourse(models.Model):
    _inherit = 'op.course'
    _description = 'Anyaca plus'

    anyaca_id=fields.Many2one('colegio.anyaca',string='Año academico')
    nivel_id=fields.Many2one('colegio.nivel',string='Nivel')
    batch_id=fields.Many2one('op.batch',string='Batch',required=True)
