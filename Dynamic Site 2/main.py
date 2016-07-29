'''
Simeon Smith
DPW1607
07-22-16
Dynamic Site
'''

import webapp2
#Import data classes.
from data import Contact, Data
#Import page classes.
from pages import Page, mainPage, contactPage

#MAIN HANDLER CLASS
class MainHandler(webapp2.RequestHandler):
    def get(self):

        #Create an instance of the data class and set it to data.
        data = Data()            #Multiple object class.
        
        #Use an for statement to loop through the contact list and match the contact up to the GET. This allows any number of contacts.
        #If there is a GET.
        if self.request.GET:
            #Loop throught the contact list.
            for c in data.contacts.list:
                #If the contact_name key from the GET request equals the first_name and last_name of the contact...
                if self.request.GET['contact_name'] == c.first_name + ' ' + c.last_name:
                    #Use the contactPage class as the page.
                    page = contactPage()
                    #Make the title of the page the first and last name with - Contacts
                    page.title = c.first_name + ' ' + c.last_name + " - Contacts"
                    #Use style.css for the css.
                    page.css = "style.css"
                    #Make the header of the page Contacts
                    page.h1 = "Contacts"
                    #Pass the contact to the contact attribute of the page.
                    page.contact = c
                    #Set the main content of the page to the contact html.
                    page.main_content = page.contact_html
        #Otherwise if no GET.
        else:
            #Use the mainPage class as the page.
            page = mainPage()
            #Make the title fo the page Contacts
            page.title = "Contacts"
            #Use the style.css file.
            page.css = "style.css"
            #Make the header the same as the title.
            page.h1 = page.title
            #For each contact in the list.
            for c in data.contacts.list:
                #Use the create_contact method from the page instance of mainPage to create a contact in the list.
                page.create_contact(c.first_name, c.last_name)
            #Set the main content of the page to the contact list.
            page.main_content = page.contact_list
        
        #Write the html attribute from the page to the browser.
        self.response.write(page.html)
        
#Setup the app for Google App Launcher.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
