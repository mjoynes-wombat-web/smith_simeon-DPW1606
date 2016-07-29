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
from data import Contact, DataMultiObject, DataMultiClass
from lib import contactLib
from pages import Page, mainPage, contactPage
import datetime

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #data = DataMultiObject()
        data = DataMultiClass()
        
        if self.request.GET:
            page = contactPage()
            for c in data.contacts.list:
                if self.request.GET['contact_name'] == c.first_name + ' ' + c.last_name:
                    page = contactPage()
                    page.title = c.first_name + ' ' + c.last_name + " - Contacts"
                    page.css = "style.css"
                    page.h1 = "Contacts"
                    page.contact = c
                    page.main_content = page.contact_html

        else:
            page = mainPage()
            page.title = "Contacts"
            page.css = "style.css"
            page.h1 = page.title
            for c in contacts.list:
                page.create_contact(c.first_name, c.last_name)
                print page.contact_list
            page.main_content = page.contact_list

        self.response.write(page.html)

        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
