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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        contacts = contactLib()

        c1 = Contact()
        c1.add_contact("Simeon", "Smith", 15092806173, "Wombat Web Design", "Owner/Designer", "11/15/88", "07/25/16")
        contacts.add_contact(c1)

        c2 = Contact()
        c2.add_contact("James", "Thompson", 13472817543, "Design Bright", "Web Developer", "02/11/10", "03/22/15")
        contacts.add_contact(c2)

        c3 = Contact()
        c3.add_contact("Neesa", "King", 12814273819, "Purfect Logos", "Screen Printer", "09/02/11", "12/10/15")
        contacts.add_contact(c3)

        c4 = Contact()
        c4.add_contact("Daryl", "Perkins", 13247561821, "K-L Mfg. Co.", "Manager", "08/17/13", "07/22/16")
        contacts.add_contact(c4)

        c5 = Contact()
        c5.add_contact("Maria", "Joynes", 12738539238, "Coldwell Banker", "Marketing Director", "04/22/10", "09/12/11")
        contacts.add_contact(c5)

        print contacts.list[1].first_contact

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
