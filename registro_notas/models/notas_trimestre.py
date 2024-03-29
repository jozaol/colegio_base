from odoo import fields , models  

class Trimestre(models.Model):
    _name = 'colegio.trimestre'
    _description = 'Trimestre'


    trimestre_id= fields.Char(string='Código del Trimestre')    
    name=fields.Selection([('Primer Trimestre','Primer Trimestre'),
    ('Segundo Trimestre','Segundo Trimestre'),
    ('Tercer Trimestre','Tercer Trimeste')],string='Trimestre' )
    anyaca_id=fields.Many2one('colegio.anyaca',string='Año Académico')
