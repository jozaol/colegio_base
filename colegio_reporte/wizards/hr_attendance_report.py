# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import date, datetime, timedelta

import logging
_logger = logging.getLogger(__name__)

class HrAttendanceReport(models.TransientModel):
    _name = 'hr.attendance.report'
    _description = "Reporte de Asistencias"

    employee_id = fields.Many2one('hr.employee', string="Empleado", required=True)
    date_start = fields.Date(string="Desde", required=True)
    date_end = fields.Date(string="Hasta", required=True)

    @api.multi
    def generate_report(self):
        inicio = datetime.strptime((str(self.date_start)+' 00:00:00'), "%Y-%m-%d %H:%M:%S")
        final = datetime.strptime((str(self.date_end)+' 23:59:59'), "%Y-%m-%d %H:%M:%S")
        asistencias = self.env['hr.attendance'].search([
            ('employee_id','=',self.employee_id.id),
            ('check_in','>=',inicio),('check_out','<=',final)])

        data = []
        for a in asistencias:
            row = {}
            fecha_entrada = a.check_in + timedelta(hours=-5)
            fecha_salida = a.check_out + timedelta(hours=-5)
            row['fecha'] = datetime.strftime(fecha_entrada, "%Y-%m-%d")
            row['entrada'] = datetime.strftime(fecha_entrada, "%H:%M")
            row['salida'] = datetime.strftime(fecha_salida, "%H:%M")
            horarios = a.employee_id.resource_calendar_id.mapped('attendance_ids')
            entrada_ok = horarios.filtered(lambda x: str(x.dayofweek)==str(int(fecha_entrada.strftime("%w"))-1)).hour_from
            salida_ok = horarios.filtered(lambda x: str(x.dayofweek)==str(int(fecha_salida.strftime("%w"))-1)).hour_to
            entrada_ok = '{0:02.0f}:{1:02.0f}'.format(*divmod(entrada_ok * 60, 60))
            salida_ok = '{0:02.0f}:{1:02.0f}'.format(*divmod(salida_ok * 60, 60))
            entrada_ok = fecha_entrada.strftime("%Y-%m-%d")+' '+entrada_ok+':00'
            salida_ok = fecha_salida.strftime("%Y-%m-%d")+' '+salida_ok+':00'
            diff_entrada = fecha_entrada - datetime.strptime(entrada_ok,"%Y-%m-%d %H:%M:%S")
            diff_salida = fecha_salida - datetime.strptime(salida_ok,"%Y-%m-%d %H:%M:%S")
            diff_permanencia = fecha_entrada - fecha_salida
            row['tardanza'] = int(diff_entrada.days * 1440 + diff_entrada.seconds/60)
            salida_anti = int(diff_salida.days * 1440 + diff_salida.seconds/60)
            row['anticipada'] = (salida_anti*-1) if salida_anti<0 else 0
            row['permanencia'] = int(diff_permanencia.days * 1440 + diff_permanencia.seconds/60)
            
            _logger.debug(diff_entrada)
            _logger.debug(diff_salida)
            _logger.debug(diff_salida.days * 1440)
            _logger.debug(diff_salida.seconds/60)
