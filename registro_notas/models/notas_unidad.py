from odoo import fields , models  ,api

class Unidad(models.Model):

    _name = 'colegio.unidad'
    _description = 'Unidad'


    name=fields.Selection([
    ('Primera Unidad','Primera Unidad'),
    ('Segunda Unidad','Segunda Unidad'),
    ('Tercera Unidad','Tercera Unidad'),
    ('Cuarta Unidad','Cuarta Unidad'),
    ('Quinta Unidad','Quinta Unidad'),
    ('Sexta Unidad','Sexta Unidad'),
    ('Septima Unidad','Septima Unidad'),
    ('Octava Unidad','Octava Unidad'),
    ('Novena Unidad','Novena Unidad'),],string='Unidad')
    trimestre_id=fields.Many2one('colegio.trimestre',string='Trimestre')
    anyaca_id=fields.Many2one('colegio.anyaca',string='Año Académico')
    unidad_id= fields.Char(string='Código de la Unidad')
    f_inicio= fields.Date(string='Fecha  Inicio')
    f_fin=fields.Date(string='Fecha Fin')
    stat_abierto=fields.Boolean(string='Abierto', deafult=False)
