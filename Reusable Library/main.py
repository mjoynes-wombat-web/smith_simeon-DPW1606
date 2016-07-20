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
from library import productData, Product, CompareProduct

class MainHandler(webapp2.RequestHandler):
    def get(self):

        products = productData()

        p1 = Product()
        p1.add_product("Shells & White Cheddar", "Annie's", 16.17, 4.5, "lb")
        products.add_to_array(p1)

        p2 = Product()
        p2.add_product("Three Cheesy Mini-Shell Pasta", "Kraft", 9.73, 3.625, "lb")
        products.add_to_array(p2)

        p3 = Product()
        p3.add_product("Organic Shells and Cheese", "Back to Nature", 3.11, 6, "oz")
        products.add_to_array(p3)

        p4 = Product()
        p4.add_product("Shells & White Cheddar", "Pasta Roni", 1.00, 6.2, "oz")
        products.add_to_array(p4)
        
        pg = Page()
        
        
        if self.request.GET:
            compare_products = productData()

            new_product = CompareProduct()
            new_product.name = self.request.GET['pName']
            new_product.brand = self.request.GET['pBrand']
            new_product.price = self.request.GET['pPrice']
            new_product.weight = self.request.GET['pWeight']
            new_product.weight_unit = self.request.GET['pUnit']
            new_product.calc_cost_oz()
            
            compare_products.add_to_array(new_product)

            for p in products.items:
                cp = CompareProduct()
                cp.add_product(p.name, p.brand, p.price, p.weight, p.weight_unit)
                compare_products.add_to_array(cp)

            compare = Compare()

            for p in compare_products.items:
                new_column = compareColumn()
                new_column.ounce_price_row = p.cost_oz
                new_column.name_row = p
                new_column.brand_row = p
                new_column.price_row = p
                new_column.weight_row = p
                compare.add_product_column(new_column)

            '''for p in products.items:
                comp_product = CompareProduct()

                price_ounce = comp_product.calc_cost_oz(p.price, p.weight, p.weight_unit)

                new_column = compareColumn()
                
                new_column.ounce_price_row = price_ounce
                new_column.name_row = p
                new_column.brand_row = p
                new_column.price_row = p
                new_column.weight_row = p

                compare.add_product_column(new_column)'''
                
                

            compare_html = compare.create_compare(compare)
            html = pg.create_page(compare.css, compare_html)
            print html


        else:
            form = Form()
            form_html = form.create_form(products.items)
            html = pg.create_page(form.css, form_html)


        
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
