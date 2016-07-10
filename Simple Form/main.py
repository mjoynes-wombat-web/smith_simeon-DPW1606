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

        if self.request.GET:
            fname = self.request.GET['fname']
            lname = self.request.GET['lname']
            name = fname + ' ' + lname
            title = self.request.GET['job_title']
            email = self.request.GET['email']
            phone1 = self.request.GET['phone1']
            phone2 = self.request.GET['phone2']
            phone3 = self.request.GET['phone3']
            phone_style = self.request.GET['phone_sep']

            if phone_style == "classic":
                phone = "(" + str(phone1) + ") " + str(phone2) + "-" + str(phone3)
            elif phone_style == "dot":
                phone = str(phone1) + "." + str(phone2) + "." + str(phone3)
            elif phone_style == "dash":
                phone = str(phone1) + "-" + str(phone2) + "-" + str(phone3)
            street = self.request.GET['street']
            city = self.request.GET['city']
            zip_code = self.request.GET['zip_code']

            city = city + ' ' + zip_code

            card_page = page.card_page

            card_page = card_page.format(**locals())

            self.response.write(card_page)
        else:
            form_page = page.form_page
            self.response.write(form_page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
