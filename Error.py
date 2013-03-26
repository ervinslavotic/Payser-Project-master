import webapp2
from google.appengine.api import users
import jinja2
import os
import string


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Error(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user() 
        if user:
            
            #set stylesheets needed per page 
            specific_urls = """
                <link type="text/css" rel="stylesheet" href="/stylesheets/""" + self.__class__.__name__ + """.css" />
            """
            
            
            #add the page query to the html
            url = self.request.url
            url = string.split(url, '/')
            Error_template_values = {
                'page': url[len(url) - 1]
            }
            
            template = jinja_environment.get_template('Page_Content/error.html')
            Error_template = template.render(Error_template_values)
            
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
                'content': Error_template
            }
           
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect('/')

app = webapp2.WSGIApplication([('/.*', Error)], debug=True)
