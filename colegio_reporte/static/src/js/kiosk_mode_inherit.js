odoo.define('asistencia.kiosk_mode_inherit', function (require) {
    "use strict";
    
    var KioskMode = require('hr_attendance.kiosk_mode');    

    KioskMode.include({
        events: {
            "click .o_hr_attendance_button_employees": function(){
                this.do_action('hr_attendance.hr_employee_attendance_action_kanban'); 
            },
            "click .op_button_students": function(){
                this.do_action('openeducat_core.act_open_op_student_view_2');
            },
        },
    });
});