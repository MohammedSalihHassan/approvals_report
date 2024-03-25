from odoo import models, fields, api, _
from odoo.exceptions import UserError

class EmployeeInfo(models.Model):
	_name='hr.employee'
	_inherit='hr.employee'


	employee_no = fields.Char('Employee No')