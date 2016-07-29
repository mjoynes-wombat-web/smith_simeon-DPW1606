'''
Simeon Smith
DPW1607
07-22-16
Dynamic Site
'''

#REQUIREMENTS
#!5 pages that are generated based on a query refence to the page data in the URL.
#!A main "home" page.
#!The pages are accessed from link "buttons".
#!Use some of the data in a calculation.

    #main.py
        #!MainHandler class
            #!Contains instances of data and page class.
            #!Transfer the information between the data and page classes.
            #!Only place self.request should be.

    #!data.py
        #!DataObject class
        #!5 data objects created from the above class

    #!pages.py
        #!Page class
            #!Contains general HTML templates
        #!ContentPage class
            #!Inherits from the page class
            #!Adds custom templates specific to this application

    #!lib.py
        #!Optional for extra credit.

#!Professionaly Designed
#Comment code in detail
#Commit 20 times.
#!No frameworks.
#!No global variables
#!NO ERRORS
#!Unique and Original

import webapp2
#Import data classes.
from data import Contact, DataMultiObject, DataMultiClass
#Import page classes.
from pages import Page, mainPage, contactPage

#MAIN HANDLER CLASS
class MainHandler(webapp2.RequestHandler):
    def get(self):

        #data = DataMultiClass()            #Uncomment to use the multiple classes class.
        data = DataMultiObject()            #Multiple object class.
        
        '''#UNCOMMENT TO USE INDIVIDUAL IF STATEMENTS AND COMMENT FOR LOOP SECTION
        #Use if statements to find contact. Must add new if statement for every contact.
        #If GET request.
        if self.request.GET:
            #If GET request contact_name key is equal to the first contact in the list first name and last name.
            if self.request.GET['contact_name'] == data.contacts.list[0].first_name + ' ' + data.contacts.list[0].last_name:
                #Use the contactPage class as the page.
                page = contactPage()
                #Make the title of the page the first and last name with - Contacts
                page.title = data.contacts.list[0].first_name + ' ' + data.contacts.list[0].last_name + " - Contacts"
                #Use style.css for the css.
                page.css = "style.css"
                #Make the header of the page Contacts
                page.h1 = "Contacts"
                #Pass the contact to the contact attribute of the page.
                page.contact = data.contacts.list[0]
                #Set the main content of the page to the contact html.
                page.main_content = page.contact_html
            #If GET request contact_name key is equal to the second contact in the list first name and last name.
            elif self.request.GET['contact_name'] == data.contacts.list[1].first_name + ' ' + data.contacts.list[1].last_name:
                #Use the contactPage class as the page.                
                page = contactPage()
                #Make the title of the page the first and last name with - Contacts
                page.title = data.contacts.list[1].first_name + ' ' + data.contacts.list[1].last_name + " - Contacts"
                #Use style.css for the css.
                page.css = "style.css"
                #Make the header of the page Contacts
                page.h1 = "Contacts"
                #Pass the contact to the contact attribute of the page.
                page.contact = data.contacts.list[1]
                #Set the main content of the page to the contact html.
                page.main_content = page.contact_html
            #If GET request contact_name key is equal to the third contact in the list first name and last name.
            elif self.request.GET['contact_name'] == data.contacts.list[2].first_name + ' ' + data.contacts.list[2].last_name:
                #Use the contactPage class as the page.
                page = contactPage()
                #Make the title of the page the first and last name with - Contacts
                page.title = data.contacts.list[2].first_name + ' ' + data.contacts.list[2].last_name + " - Contacts"
                #Use style.css for the css.
                page.css = "style.css"
                #Make the header of the page Contacts
                page.h1 = "Contacts"
                #Pass the contact to the contact attribute of the page.
                page.contact = data.contacts.list[2]
                #Set the main content of the page to the contact html.
                page.main_content = page.contact_html
            #If GET request contact_name key is equal to the fourth contact in the list first name and last name.
            elif self.request.GET['contact_name'] == data.contacts.list[3].first_name + ' ' + data.contacts.list[3].last_name:
                #Use the contactPage class as the page.
                page = contactPage()
                #Make the title of the page the first and last name with - Contacts
                page.title = data.contacts.list[3].first_name + ' ' + data.contacts.list[3].last_name + " - Contacts"
                #Use style.css for the css.
                page.css = "style.css"
                #Make the header of the page Contacts
                page.h1 = "Contacts"
                #Pass the contact to the contact attribute of the page.
                page.contact = data.contacts.list[3]
                #Set the main content of the page to the contact html.
                page.main_content = page.contact_html
            #If GET request contact_name key is equal to the fifth contact in the list first name and last name.
            elif self.request.GET['contact_name'] == data.contacts.list[4].first_name + ' ' + data.contacts.list[4].last_name:
                #Use the contactPage class as the page.
                page = contactPage()
                #Make the title of the page the first and last name with - Contacts
                page.title = data.contacts.list[4].first_name + ' ' + data.contacts.list[4].last_name + " - Contacts"
                #Use style.css for the css.
                page.css = "style.css"
                #Make the header of the page Contacts
                page.h1 = "Contacts"
                #Pass the contact to the contact attribute of the page.
                page.contact = data.contacts.list[4]
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
        '''
        
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
