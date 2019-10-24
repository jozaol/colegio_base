from odoo import fields , models

class MesesPension(models.Model):
    _name='colegio.meses_pension'
    _description='Meses Pension'

    name=fields.Char(string='Meses Pension')
    nivel_id=fields.Many2one('colegio.nivel',string='Nivel')
    anyaca_id=fields.Many2one('colegio.anyaca',string='Año Academico')
    mes_id=fields.Char(string='Mes')