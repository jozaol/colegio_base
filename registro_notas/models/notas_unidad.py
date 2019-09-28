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
    ('Novena Unidad','Novena Unidad'),],string='Unidad',required=True)
    trimestre_id=fields.Many2one('colegio.trimestre',string='Trimestre',required=True)
    anyaca_id=fields.Many2one('colegio.anyaca',string='Año Académico',required=True)
    unidad_id= fields.Char(string='Código de la Unidad', required=True)
    f_inicio= fields.Date(string='Fecha  Inicio', required=True)
    f_fin=fields.Date(string='Fecha Fin', required=True)
    stat_abierto=fields.Boolean(string='Abierto', deafult=False)
