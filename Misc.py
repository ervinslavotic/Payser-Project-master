import webapp2
import jinja2
import os
import Models

from google.appengine.ext import db
from google.appengine.api import users


payslips = db.GqlQuery("SELECT * "
                "FROM Payslip "
                "WHERE ANCESTOR IS :1 ",
                Models.payslip_key(users.get_current_user().user_id()))
    
income = 0
tax = 0
payslip_count = 0            
for payslip in payslips:
    income+= payslip.income
    tax += payslip.tax
    payslip_count += 1
    
employee = Models.Employee()
 
employee.userid = user.user_id()
employee.income = income
employee.tax = tax
employee.net = income - tax
employee.account_type = "employee"

employee.put()


"""
        if self.request.POST['file']:
                file_name = files.blobstore.create(mime_type='application/octet-stream')
                with files.open(file_name, 'a') as f:
                    f.write('data')
                files.finalize(file_name)
                blob_key = files.blobstore.get_blob_key(file_name)
"""