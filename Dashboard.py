import webapp2
import jinja2
import os
import Models

from google.appengine.api import users
from google.appengine.ext import db

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Dashboard(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user() 
        
        if user:
            
            pasyer_users = db.GqlQuery("SELECT * "
                "FROM Site_User "
                "WHERE userid = :1 ",
                user.user_id())
            
            current_user = False
            for pasyer_user in pasyer_users:
                current_user = pasyer_user

            if not current_user:
                self.redirect("/settings")
            else:
            
                payslips = db.GqlQuery("SELECT * "
                    "FROM Payslip "
                    "WHERE ANCESTOR IS :1 ",
                    Models.payslip_key(user.user_id()))
        
                income = 0
                tax = 0
                payslip_count = 0            
                for payslip in payslips:
                    income+= payslip.income
                    tax += payslip.tax
                    payslip_count += 1
                    
                files = db.GqlQuery("SELECT * "
                    "FROM File "
                    "WHERE ANCESTOR IS :1 ",
                    Models.file_key(user.user_id()))
                file_count = 0    
                for file in files:
                    file_count += 1
                    
    
                #set stylesheets needed per page 
                specific_urls = """
                    <link type="text/css" rel="stylesheet" href="/stylesheets/""" + self.__class__.__name__ + """.css" />
                """
                
                dashboard_template_values = {
                    'name': current_user.name,
                    'email': current_user.email,
                    'account_type': current_user.account_type,
                    'payslip_quantity': payslip_count,
                    'file_quantity': file_count,
                    'income': income,
                    'tax': tax,
                    'net': income - tax
                }
                
                template = jinja_environment.get_template('Page_Content/dashboard.html')
                dashboard_template = template.render(dashboard_template_values)
                
                url = users.create_logout_url(self.request.uri)
                nav = """
                <nav>
                    <ul>
                        <li><a href="/dashboard">Dashboard</a></li>
                        <li><a href="#">Design</a></li>
                        <li><a href="#">About</a></li>
                        <li><a href="%s">Logout</a></li>
                    </ul>
                </nav>
                """ % url
               
                    
                template_values = {
                    'specific_urls':specific_urls,
                    'nav': nav,
                    'content': dashboard_template
                }
               
                template = jinja_environment.get_template('index.html')
                self.response.out.write(template.render(template_values))
        else:
            self.redirect('/')

app = webapp2.WSGIApplication([('/dashboard', Dashboard)], debug=True)
