# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EmployeeDetails(models.Model):

    _name = 'employee.details'

    name = fields.Char(string="First Name", required='True')
    last_name = fields.Char(string="Last Name")
    dob = fields.Date(default=datetime.datetime.today())
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    street = fields.Char(string="street 1")
    city = fields.Many2one('employee.city', string="City", ondelete="cascade")
    postal_code = fields.Char(string="Postal Code")
    state = fields.Many2one('res.country.state', string="State")
    country = fields.Many2one('res.country', ondelete="cascade")
    email_id = fields.Char()
    mobile = fields.Char(size=10)
    color = fields.Integer('Color Index')
    project_id = fields.One2many("employee.projects", "employee_id", string="Projects")
    employee_edu_id = fields.One2many('employee.education.details', 'employee_id', string='Education Detail')
    state = fields.Selection([
        ('active', 'Active'),
        ('deactive', 'DeActive'),
        ('block', 'Block'),
        ], string='Status', default='active')

    @api.multi
    def action_deactive(self):
        self.write({'state': 'deactive'})

    def action_block(self):
        self.write({'state': 'block'})

    def action_active(self):
        self.write({'state': 'active'})


class EmployeeEducationDetails(models.Model):

    _name = 'employee.education.details'

    employee_id = fields.Many2one('employee.details', ondelete="cascade")
    degree = fields.Char()
    university_name = fields.Char()
    passing_year = fields.Date()
    percentage_cgpa = fields.Char()


class ProjectDetails(models.Model):

    _name = 'employee.projects'

    name = fields.Char(stirng="Project Name")           
    employee_id = fields.Many2one("employee.details")
    languages = fields.Many2many("languages")
    project_detail = fields.Char()
    color = fields.Integer('Color Index')


class Languages(models.Model):

    _name = 'languages'

    language = fields.Char()


class EmployeeCity(models.Model):

    _name = "employee.city"

    name = fields.Char(string="City")