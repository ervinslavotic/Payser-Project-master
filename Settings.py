import webapp2
import jinja2
import os
import string
import datetime
import Models


from google.appengine.api import users
from google.appengine.ext import db



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Settings(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user() 
        if user:
            
            #set stylesheets needed per page 
            specific_urls = """
                <link type="text/css" rel="stylesheet" href="/stylesheets/""" + self.__class__.__name__ + """.css" />
                <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
                <script type="text/javascript" src="/js/validate.js"></script>
                <script type="text/javascript" src="/js/upload_form_account.js"></script>
            """
            
            
            #add the page query to the html
            Settings_template_values = {
                'email': user.email()
            }
            
            
            template = jinja_environment.get_template('Page_Content/settings.html')
            Settings_template = template.render(Settings_template_values)
            
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
                'content': Settings_template
            }
           
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect('/')
            
            
    def post(self):
        
        user = users.get_current_user()
        
        payser_users = db.GqlQuery("SELECT * "
                "FROM Site_User "
                "WHERE userid = :1 ",
                user.user_id())
        
        current_user = False
        
        for payser_user in payser_users:
            current_user = payser_user

        if not current_user:
            current_user = Models.Site_User()
             
            current_user.userid = user.user_id()
            current_user.name = self.request.POST['name']
            current_user.email = self.request.POST['email']
            current_user.company = self.request.POST['company']
            current_user.account_type = self.request.POST['type']
            
            self.response.out.write( current_user.userid + "<br/>" )
            self.response.out.write(current_user.name + "<br/>")
            self.response.out.write(current_user.email + "<br/>")
            self.response.out.write(current_user.company + "<br/>")
            self.response.out.write(current_user.account_type + "<br/>")
    
            current_user.put()
        else:
            current_user.userid = user.user_id()
            current_user.name = self.request.POST['name']
            current_user.email = self.request.POST['email']
            current_user.company = self.request.POST['company']
            current_user.account_type = self.request.POST['type']
            
            self.response.out.write( current_user.userid + "<br/>" )
            self.response.out.write(current_user.name + "<br/>")
            self.response.out.write(current_user.email + "<br/>")
            self.response.out.write(current_user.company + "<br/>")
            self.response.out.write(current_user.account_type + "<br/>")
            
            current_user.put()

app = webapp2.WSGIApplication([('/settings', Settings)], debug=True)
