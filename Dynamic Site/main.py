'''
Simeon Smith
DPW1607
07-22-16
Dynamic Site
'''

#REQUIREMENTS
#5 pages that are generated based on a query refence to the page data in the URL.
#A main "home" page.
#The pages are accessed from link "buttons".
#Use some of the data in a calculation.

    #main.py
    #MainHandler class
        #Contains instances of data and page class.
        #Transfer the information between the data and page classes.
        #Only place self.request should be.

    #data.py
    #DataObject class
    #5 data objects created from the above class

    #pages.py
    #Page class
        #Contains general HTML templates
    #ContentPage class
        #Inherits from the page class
        #Adds custom templates specific to this application

    #lib.py
        #Optional for extra credit.

#Professionaly Designed
#Comment code in detail
#Commit 20 times.
#No frameworks.
#No global variables
#NO ERRORS
#Unique and Original

import webapp2
from data import Contact
from lib import contactLib
import datetime

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        contacts = contactLib()

        c1 = Contact()
        c1.add_contact("Simeon", "Smith", 15092806173, "Wombat Web Design", "Owner/Designer", "11/15/1988", "07/25/2016")
        contacts.add_contact(c1)

        c2 = Contact()
        c2.add_contact("James", "Thompson", 13472817543, "Design Bright", "Web Developer", "02/11/2010", "03/22/2015")
        contacts.add_contact(c2)

        c3 = Contact()
        c3.add_contact("Neesa", "King", 12814273819, "Purfect Logos", "Screen Printer", "09/02/2011", "12/10/2015")
        contacts.add_contact(c3)

        c4 = Contact()
        c4.add_contact("Daryl", "Perkins", 13247561821, "K-L Mfg. Co.", "Manager", "08/17/2013", "07/22/2016")
        contacts.add_contact(c4)

        c5 = Contact()
        c5.add_contact("Maria", "Joynes", 12738539238, "Coldwell Banker", "Marketing Director", "04/22/2010", "09/12/2011")
        contacts.add_contact(c5)

        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
