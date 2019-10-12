{
    'name': 'Asistencia',
    'version': '1.0',
    'author': 'Jose Zambrano',
    'depends': ['base','hr_attendance','openeducat_core'],
    'data': [
        'report/hr_attendance_report.xml',
        'report/hr_attendance_template.xml',
        'security/ir.model.access.csv',
        'views/web_assets_backend_template.xml',
        'wizards/hr_attendance_report_view.xml',
        'views/menus_view.xml',
    ],
    'qweb': [
        'static/src/xml/attendance.xml',
    ],
}