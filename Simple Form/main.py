'''
Simeon Smith
DPW1607
07-09-16
Simple Form
'''

#REQUIREMENTS
    #Collect 5 pieces of information.
        #One text based
        #One radio button
        #One select item
    #Organize HTML elements in page class.
    #Use GET method to deliver info gathered.
    #List information after GET.
    #Create a polished and professional design.
    #Comment code.
    #Make 6 commits to GitHub.
    #No global variables.
    #No errors.
    #No frameworks.
    
import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()

        form_page = page.form_page

        self.response.write(form_page);

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
