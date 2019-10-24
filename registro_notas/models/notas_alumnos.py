from odoo import fields ,models

class NotasAlumno(models.Model):
    _name='colegio.notas_alumno'
    name=fields.Many2one('op.student',string='Alumno')
    student_id=fields.Many2one('op.student',string='Alumno')
##    nota1=fields.Integer(string='Nota1')
##    nota2=fields.Integer(string='Nota2')   
##    nota3=fields.Integer(string='Nota3')
##    nota4=fields.Integer(string='Nota4') 
    alumno_nota=fields.Integer(string='Nota')
    obs=fields.Char(string='Obserbacion')