from odoo import fields ,models

class Niveles(models.Model):
    _name='colegio.nivel'
    _description='Nivel'

    name=fields.Selection([('Nivel 1','Nivel 1'),('Nivel 2','Nivel 2'),('Nivel 3','Nivel 3')],string='Nivel')
    codigo_id=fields.Char(string='Codigo')
    anyaca_id=fields.Many2one('colegio.anyaca',string='Año Academico')
#   invoice_line_id=fields.Many2one('account.invoice',string='Invoice')