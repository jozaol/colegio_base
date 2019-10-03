{
'name': 'Colegio base',
'description': 'Anexo de campos course.',
'author': 'Andre Zambrano',
'data': [
    'security/ir.model.access.csv',
    'security/course_security.xml',
    'security/subject_security.xml',
    'views/course_view.xml',
    'views/subject_view.xml',
    'views/batch_view.xml',

],
'depends': [
    'openeducat_core',
],
'application': False,
}