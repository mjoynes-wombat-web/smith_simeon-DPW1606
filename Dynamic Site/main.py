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
from data import c1

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        print c1.first_name

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
