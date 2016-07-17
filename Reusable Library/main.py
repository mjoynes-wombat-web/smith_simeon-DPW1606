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
import urllib2
from pages import Page, Form
from data import Product

class MainHandler(webapp2.RequestHandler):
    def get(self):

        products = []

        p1 = Product()
        p1.name = "Shells & White Cheddar"
        p1.brand = "Annie's'"
        p1.price = 16.17
        p1.weight = 4.5;
        p1.weight_unit = "lb"
        products.append(p1)

        p2 = Product()
        p2.name = "Three Cheesy Mini-Shell Pasta"
        p2.brand = "Kraft"
        p2.price = 9.73
        p2.weight = 3.625
        p2.weight_unit = "lb"
        products.append(p2)

        p3 = Product()
        p3.name = "Organic Shells and Cheese"
        p3.brand = "Back to Nature"
        p3.price = 3.11
        p3.weight = 6
        p3.weight_unit = "oz"
        products.append(p3)

        p4 = Product()
        p4.name = "Shells & White Cheddar"
        p4.brand = "Pasta Roni"
        p4.price = 1.00
        p4.weight = 6.2
        p4.weight_unit = "oz"
        products.append(p4)
        
        pg = Page()
        form = Form()

        
        
        
        if self.request.GET['form'] == "addProduct":
            new_product = Product()
            new_product.name = self.request.GET['pName']
            new_product.brand = self.request.GET['pBrand']
            new_product.price = self.request.GET['pPrice']
            new_product.weight = self.request.GET['pWeight']
            new_product.weight_unit = self.request.GET['pUnit']

            products.append(new_product)


        form_html = form.create_form(products)
        print form
        html = pg.create_page(form.css, form_html)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
