{   
 'name': 'custom_approvals_report',
 'summary': """This module will add approvals report""",
 'version': '10.0.1.0.0',
 'description': """This module will add approvals report""",
 'author': 'ALIAICT@IT',
 'company': 'ALIAICT',
 'website': 'https://www.aliaict.com',
 'category': '',  
 'depends': ['base','hr_saudi_approvals'],
 'license': 'AGPL-3',
 'data': [
            'views/employee_info_view.xml',
            'report/report_view.xml',
            'report/template/header_footer_template.xml',
            'report/template/custom_approval_report_template.xml'
        ],
 'demo': [],
 'installable': True,
 'auto_install': False,
 'application': True,
}