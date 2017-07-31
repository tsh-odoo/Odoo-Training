# -*- coding: utf-8 -*-


from odoo.tests.common import TransactionCase


class TestEmployee(TransactionCase):

    def setUp(self):
        super(TestEmployee, self).setUp()
        self.EmployeeDetails = self.env['employee.details']
        self.EmployeeEducationDetails = self.env['employee.education.details']
        self.EmployeeCity = self.env['employee.city']
        self.EmployeeLanguages = self.env['languages']
        self.ProjectDetails = self.env['employee.projects']

    def test_employee(self):
        """Test case run """
        student_degree_tenth = self.EmployeeEducationDetails.create({
            'name': '10th'
        })
        student_degree_eleventh = self.EmployeeEducationDetails.create({
            'name': '12th'
        })
        print "\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SUCCESS Employee Degree\n\n"
        student_city_meh = self.EmployeeCity.create({
            'name': 'Meh'
        })
        print "\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SUCCESS Employee City\n\n"

        student_degree_univ_gtu = self.EmployeeEducationDetails.create({
            'university_name': 'GTU'
        })
        print "\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SUCCESS Univerity Name\n\n"
        student_languages_c = self.EmployeeLanguages.create({
            'name': 'Python'
            })
        print "\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SUCCESS Employee Project Language\n\n"

        student_project_nirmalya = self.ProjectDetails.create({
            'name': 'Obstacle_Detection',
            'languages_ids': [(0, 0, {
                    'name': student_languages_c.id,
                })],
            'project_detail': 'IOT'
        })
        print "\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SUCCESS Project Creation\n\n"
        # I create a new Employee persosnal detail
        student = self.EmployeeDetails.create({
            'name': 'Demo',
            'gender': 'male',
            'email_id': 'foo@yourcompany.example.com',
            'project_ids': [(0, 0, {
                'name': student_project_nirmalya.id
                })]
        })
        student.action_deactive()
        self.assertTrue(student.state == 'deactive', 'state is wrong')
        student.action_block()

        print "\n\nCongratulations,Test case Successfully passed\n\n"