# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import date, datetime, timedelta
from odoo.exceptions import UserError

class HrAttendanceReport(models.TransientModel):
    _name = 'hr.attendance.report'
    _description = "Reporte de Asistencias"

    employee_id = fields.Many2one('hr.employee', string="Empleado", required=True)
    date_start = fields.Date(string="Desde", required=True)
    date_end = fields.Date(string="Hasta", required=True)

    @api.multi
    def generate_report(self):
        return self.env.ref('asistencia.action_report_hr_attendance').report_action(self)

    @api.model
    def get_data(self, employee, date_start, date_end):
        inicio = datetime.strptime((str(date_start)+' 00:00:00'), "%Y-%m-%d %H:%M:%S")
        final = datetime.strptime((str(date_end)+' 23:59:59'), "%Y-%m-%d %H:%M:%S")
        asistencias = self.env['hr.attendance'].search([
            ('employee_id','=',employee.id),
            ('check_in','>=',inicio),('check_out','<=',final)])
        
        delta = self.date_end - self.date_start
        dates = []
        for i in range(delta.days + 1):
            dates.append(self.date_start + timedelta(days=i))

        print(dates)
        data = []
        for d in dates:
            a = asistencias.filtered(lambda x: x.check_in.date()==d)
            row = {}

            #OBTENIENDO LA HORA DE ENTRADA Y SALIDA FIJAS DEL EMPLEADO EN FLOAT
            horarios = self.employee_id.resource_calendar_id.mapped('attendance_ids')
            entrada = horarios.filtered(lambda x: str(x.dayofweek)==str(int(d.strftime("%w"))-1))
            salida = horarios.filtered(lambda x: str(x.dayofweek)==str(int(d.strftime("%w"))-1))
            if not entrada and not salida and not a:
                row['fecha'] = datetime.strftime(d, "%Y-%m-%d")
                row['entrada'] = ""
                row['salida'] = ""
                row['tardanza'] = 0
                row['anticipada'] = 0
                row['permanencia'] = 0
                row['estado'] = "N"
                row['horas'] = 0
                row['minutos'] = 0
                data.append(row)
                continue
            entrada_ok = entrada.hour_from
            salida_ok = salida.hour_to

            if not a:
                row['fecha'] = datetime.strftime(d, "%Y-%m-%d")
                row['entrada'] = ""
                row['salida'] = ""
                row['tardanza'] = 0
                row['anticipada'] = 0
                row['permanencia'] = 0
                row['estado'] = "F"
                row['horas'] = 0
                row['minutos'] = 0
                data.append(row)
                continue
            a = a[0]
            fecha_entrada = a.check_in + timedelta(hours=-5)
            fecha_salida = a.check_out + timedelta(hours=-5)
            row['fecha'] = datetime.strftime(fecha_entrada, "%Y-%m-%d")
            row['entrada'] = datetime.strftime(fecha_entrada, "%H:%M")
            row['salida'] = datetime.strftime(fecha_salida, "%H:%M")
            estado = "A"

            #OBTENIENDO LA ENTRADA Y SALIDA DEL EMPLEADO CONVERTIDO A FLOAT
            entrada_float = datetime.strptime(row['entrada'], "%H:%M").time()
            entrada_float = entrada_float.hour + entrada_float.minute / 60.0
            salida_float = datetime.strptime(row['salida'], "%H:%M").time()
            salida_float = salida_float.hour + salida_float.minute / 60.0

            #OBTENIENDO LA TARDANZA EN MINUTOS
            tardanza = 0
            if entrada_float > entrada_ok:
                estado = "T"
                tardanza = entrada_float - entrada_ok
                tardanza = round(tardanza * 60)

            #OBTENIENDO LA ANTICIPADA EN MINUTOS
            anticipada = 0
            if salida_float < salida_ok:
                anticipada = salida_ok - salida_float
                anticipada = round(anticipada * 60)
            
            # OBTENIENDO LA PERMANENCIA EN MINUTOS
            permanencia = 0
            if salida_float > salida_ok:
                permanencia = salida_float - salida_ok
                permanencia = round(permanencia * 60)

            row['tardanza'] = tardanza
            row['anticipada'] = anticipada
            row['permanencia'] = permanencia
            row['estado'] = estado

            # OBTENIENDO LAS HORAS Y MINUTOS QUE PERMANECIO
            diferencia_fecha = fecha_entrada - fecha_salida
            result = str(abs(diferencia_fecha)).split(":")
            row['horas'] = result[0]
            row['minutos'] = result[1]

            data.append(row)
        return data