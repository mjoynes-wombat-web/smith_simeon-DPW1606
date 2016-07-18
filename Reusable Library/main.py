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
from pages import Page, Form, Compare, compareColumn
from data import productData, Product, CalcCompare

class MainHandler(webapp2.RequestHandler):
    def get(self):

        products = productData()

        p1 = Product()
        p1.name = "Shells & White Cheddar"
        p1.brand = "Annie's"
        p1.price = 16.17
        p1.weight = 4.5;
        p1.weight_unit = "lb"
        products.add_product(p1)

        p2 = Product()
        p2.name = "Three Cheesy Mini-Shell Pasta"
        p2.brand = "Kraft"
        p2.price = 9.73
        p2.weight = 3.625
        p2.weight_unit = "lb"
        products.add_product(p2)

        p3 = Product()
        p3.name = "Organic Shells and Cheese"
        p3.brand = "Back to Nature"
        p3.price = 3.11
        p3.weight = 6
        p3.weight_unit = "oz"
        products.add_product(p3)

        p4 = Product()
        p4.name = "Shells & White Cheddar"
        p4.brand = "Pasta Roni"
        p4.price = 1.00
        p4.weight = 6.2
        p4.weight_unit = "oz"
        products.add_product(p4)
        
        pg = Page()
        
        
        if self.request.GET:

            new_product = Product()
            new_product.name = self.request.GET['pName']
            new_product.brand = self.request.GET['pBrand']
            new_product.price = self.request.GET['pPrice']
            new_product.weight = self.request.GET['pWeight']
            new_product.weight_unit = self.request.GET['pUnit']
            products.add_product(new_product)

            compare = Compare()

            for p in products.list:
                calc = CalcCompare()

                price_ounce = calc.calc_cost_oz(p.price, p.weight, p.weight_unit)

                new_column = compareColumn()
                
                new_column.ounce_price_row = price_ounce
                new_column.name_row = p
                new_column.brand_row = p
                new_column.price_row = p
                new_column.weight_row = p

                compare.add_product_column(new_column)
                
                

            compare_html = compare.create_compare(compare)
            html = pg.create_page(compare.css, compare_html)
            print html


        else:
            form = Form()
            form_html = form.create_form(products.list)
            html = pg.create_page(form.css, form_html)


        
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
