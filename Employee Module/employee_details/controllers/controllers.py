# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import base64
from logging import getLogger

_logger = getLogger(__name__)


class EmployeeDetails(http.Controller):

    @http.route('/employee_details/index', auth='public', website=True)
    def list(self, **kw):
        name = request.env['employee.details'].search([])
        return request.render('employee_details.employee_list', {
            'employees': name,
        })

    @http.route('/employee_details/<model("employee.details"):employee>', auth='public', website=True)
    def detail(self, employee=None, **kw):

        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",employee

        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",employee.name
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",employee.dob

        return request.render('employee_details.info', {
            'employee': employee
        })

    @http.route('/employee_details/edit/', type="json", website=True, auth='public')
    def get_employee_edit_form(self, employee_id=None, **kw):
        employee = request.env['employee.details'].browse(employee_id)
        return request.env.ref('employee_details.employee_edit_form').render({'employee': employee})

    @http.route('/employee_details/submit/', website=True, auth='public')
    def get_employee_submit_form(self, **kw):
        employee = request.env['employee.details'].search([('id', '=', kw['employee_id'])])
        employee.write(kw)
        print "\n\n--------employee", employee

        return request.env.ref('employee_details.info').render({'employee': employee})

    @http.route('/employee_details/get_education_details', type='json')
    def get_education_details(self, employee_id=None, **kw):
        employee_data = []
        print ">>>>>>>>>>>>>>>ed", employee_data
        employee = request.env['employee.details'].browse(employee_id)
        for std in employee.mapped('employee_edu_id'):
            employee_data.append({
                'employee_id': employee_id,
                'degree': employee.degree,
                'university_name': employee.university_name,
                'passing_year': employee.passing_year
            })
        return employee_data

    @http.route('/employee_details/create/', website=True, auth='public', method="POST")
    def add_employee(self, **kw):
        request.env['employee.details'].create(kw)
        return True