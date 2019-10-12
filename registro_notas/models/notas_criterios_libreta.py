from odoo import fields , models 

class CriteriosLibreta(models.Model):
    _name = 'colegio.criterios_libreta'
    _description = 'Criterios de la libreta'


    anyaca_id=fields.Many2one('colegio.anyaca',string='Año Académico')
    grado_id=fields.Many2one('op.batch',tring='Grado')
    criterio=fields.Text(string='Criterio')