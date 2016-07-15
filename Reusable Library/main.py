'''
Simeon Smith
DPW1607
07-15-16
Reusable Library
'''

#LIBRARY
    #Two classes minimum
    #Fully encapsulated
    #No public attributes
    #Access through getters and setters
    #3 Utility functions
        #Can perform calculations or organize info
        #Like compile movie list or calc span
        #Original

#PAGE
    #Minimum two views
    #May require two classes and have redundant code
    #Code will run twice, use condition to decide which view to render
    
    #VIEW CLASS
        #One view will contain a form to collect data
            #Must have at least 4 inputs
                #Validate with JavaSCript and HTML5
        #Second view will display information collected
        #Should contain the almost all the HTML

#Must be professionally designed
#Comment code in detail
#Make at least 15 commits
#No frameworks
#No global variables
#NO ERRORS

import webapp2
from pages import Page, Form
from data import Product

class MainHandler(webapp2.RequestHandler):
    def get(self):
        mac_cheese = Product()
        mac_cheese.name = "Mac and Cheese"
        mac_cheese.brand = "Kraft"
        mac_cheese.price = 12
        mac_cheese.weight = 5;
        mac_cheese.weight_unit = "oz"
        
        p = Page()
        form = Form()

        products = []
        products.append(mac_cheese)
        form = form.create_form(products)
        print form
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
