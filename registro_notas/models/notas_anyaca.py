from odoo import fields , models  

class Anyaca(models.Model):
    _name='colegio.anyaca'
    _description='Año academico'


    anyaca_id=fields.Char(string='Código del Año Academico',required=True)
    name=fields.Char(string='Año Academico',required=True)
    stats_abierto=fields.Boolean(string='Abierto', default=False)
    slogan=fields.Char(string="Slogan",required=True)
    anyo_fiscal=fields.Char(string="Año Fiscal",required=True)


