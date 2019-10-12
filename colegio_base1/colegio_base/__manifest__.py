{
'name': 'Colegio base',
'description': 'Anexo de campos course.',
'author': 'Andre Zambrano',
'data': [
    'security/ir.model.access.csv',
    'views/course_view.xml',
    'views/subject_view.xml',
    'views/batch_view.xml',
    'views/batch1_view.xml',

],
'depends': [
    'openeducat_core',
    'registro_notas',
],
'application': False,
}