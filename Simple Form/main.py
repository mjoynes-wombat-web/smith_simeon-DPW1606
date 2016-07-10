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
#Import the page class.
from pages import Page

#GOOGLE APP ENGINE CLASS
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Pull in the page class and store it.
        page = Page()

        #If there is a GET request store the variables from GET and write page.
        if self.request.GET:
            #NAME VARIABLES
            fname = self.request.GET['fname']               #First Name
            lname = self.request.GET['lname']               #Last Name
            name = fname + ' ' + lname                      #Concat first and last name

            #TITLE VARIABLE
            title = self.request.GET['job_title']           #Title
            #If title is empty insert a page break.
            if title == "":
                title = "<br>"
            
            #CONTACT VARIABLES
            email = self.request.GET['email']               #Email
            #PHONE NUMBER PARTS
            phone1 = self.request.GET['phone1']             #Phone section 1
            phone2 = self.request.GET['phone2']             #Phone section 2
            phone3 = self.request.GET['phone3']             #Phone section 3
            phone_style = self.request.GET['phone_sep']     #Formatting style for phone number
            #Check for the phone style type and store the results as phone
            if phone_style == "classic":                    #Format as classic
                phone = "(" + str(phone1) + ") " + str(phone2) + "-" + str(phone3)
            elif phone_style == "dot":                      #Format with dot
                phone = str(phone1) + "." + str(phone2) + "." + str(phone3)
            elif phone_style == "dash":                     #Format with dash
                phone = str(phone1) + "-" + str(phone2) + "-" + str(phone3)
            #ADDRESS PARTS
            street = self.request.GET['street']             #Street Address
            city = self.request.GET['city']                 #City
            zip_code = self.request.GET['zip_code']         #Zip Code
            #Concat city and zip code.
            city = city + ' ' + zip_code
            #Pull in the card page template from the page class.
            card_page = page.card_page
            #Format the template with the locals provided by GET
            card_page = card_page.format(**locals())
            #Write the card_page variable to the page.
            self.response.write(card_page)
        #If no GET write the form page.
        else:
            #Pull in the form pagefrom the page class.
            form_page = page.form_page
            #Write the form_page variable to the page.
            self.response.write(form_page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
