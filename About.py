import webapp2
from google.appengine.api import users
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/Page_Content"))

class About(webapp2.RequestHandler):
    def get(self):
        
        
        #set stylesheets needed per page 
        specific_urls = """
            <link type="text/css" rel="stylesheet" href="/stylesheets/""" + self.__class__.__name__ + """.css" />
        """
        
        
        myFile = open('Page_Content/about.html', 'r')
        
        #Set the nav depending on login status
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            nav = """
            <nav>
                <ul>
                    <li><a href="/dashboard">Dashboard</a></li>
                    <li><a href="/design">Design</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="%s">Logout</a></li>
                </ul>
            </nav>
            """ % url
        else:
			
            url = users.create_login_url(self.request.uri + "about")
            nav = """
            <nav>
                <ul>
                    <li><a href="/dashboard">Home</a></li>
                    <li><a href="/design">Design</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="%s">Login</a></li>
                </ul>
            </nav>
            """ % url
			
			#self.response.out.write(nav.render(start_page))
			
			
        template_values = {
            'specific_urls':specific_urls,
            'nav': nav,
            'content':myFile.read()
        }
       
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([('/about', About)], debug=True)
