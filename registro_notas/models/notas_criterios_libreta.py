from odoo import fields , models 

class CriteriosLibreta(models.Model):
    _name = 'colegio.criterios_libreta'
    _description = 'Criterios de la libreta'


    anyaca_id=fields.Many2one('colegio.anyaca',string='Año Académico',required=True)
    grado_id=fields.Many2one('op.batch',tring='Grado',required=True)
    criterio=fields.Text(string='Criterio')