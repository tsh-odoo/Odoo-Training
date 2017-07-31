odoo.define('employee_details.employee', function(require) {
'use strict';

var ajax = require('web.ajax');
var employee_widgets = require('employee_details.degree');

var EmployeeEducationDetails = employee_widgets.EmployeeEducationDetails;

$( document ).ready(function(){
    console.log('Hello from document.ready');

    $('#edit_employee').on("click", function(e){
        var employee_id = $(this).data('employee_id');
        ajax.jsonRpc("/employee_details/edit/", 'call', {'employee_id': employee_id}).then(function (result_std){
            $(".data").html(result_std);
        });
    });
    $(".o_show_degree").on("click", function(e) {
        var $this = $(this);
        var employee_id = $this.data('employee_id');
        var employee_degree = new EmployeeEducationDetails(employee_id, {});
        $this.parent().find('.details_placeholder').empty();
        employee_degree.appendTo($this.parent().find('.details_placeholder'));
    });
    $(".show_details").on("click", function(e){
        var $this = $(this);
        var employee_id = $this.data('employee_id');
        window.location.replace("/employee_details/"+employee_id);
    });
});



});