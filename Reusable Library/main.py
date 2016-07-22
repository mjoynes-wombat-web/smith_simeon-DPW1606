'''
Simeon Smith
DPW1607
07-15-16
Reusable Library
'''

import webapp2
from pages import Page, FormHTML, CompareHTML, compareColumn                                #Importing classes from pages.py
from library import productData, Product, CompareProduct                            #Importing classes from library.py

#Main Handler Class
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Adding 4 placehodler products using the Products class and it's add_product method
        p1 = Product()
        p1.add_product("Shells & White Cheddar", "Annie's", 16.17, 4.5, "lb")

        p2 = Product()
        p2.add_product("Three Cheesy Mini-Shell Pasta", "Kraft", 9.73, 3.625, "lb")

        p3 = Product()
        p3.add_product("Organic Shells and Cheese", "Back to Nature", 3.11, 6, "oz")

        p4 = Product()
        p4.add_product("Shells & White Cheddar", "Pasta Roni", 1.00, 6.2, "oz")
        #Using the productData class to hold the products for the main page.
        products = productData()
        products.add_to_array(p1)
        products.add_to_array(p2)
        products.add_to_array(p3)
        products.add_to_array(p4)
        #Using the Page class to setup the beginnings of the HTML page.
        pg = Page()
        #Checking for GET, if GET render the compare products page, otherwise render the main page.
        if self.request.GET:
            #Using the producData class to hold products for the compare page.
            compare_products = productData()
            #Creating a new product with the CompareProduct class using the info from GET and add it to the compare_products instance of the productData class.
            new_product = CompareProduct()
            new_product.add_product(self.request.GET['pName'], self.request.GET['pBrand'], self.request.GET['pPrice'], self.request.GET['pWeight'], self.request.GET['pUnit'])
            compare_products.add_to_array(new_product)
            #For each product from the main page create a new instance of the CompareProduct class.
            for p in products.items:
                cp = CompareProduct()
                #Populate the cp instance with the information from the original products.
                cp.add_product(p.name, p.brand, p.price, p.weight, p.weight_unit)
                #Add it to the compare_products instance of the productData class.
                compare_products.add_to_array(cp)
            #Using the CompareHTML class create the compare_page instance.
            compare_page = CompareHTML()
            #For each of the compare_products items created a new_column instance of the compareColumn() class.
            for p in compare_products.items:
                new_column = compareColumn()
                #Create the column using the info from the compare_products item and the creat_column method from the compareColumn class.
                new_column.create_column(p)
                #Add it to the array in the compare_page that holds the columns using the add_product_method.
                compare_page.add_product_column(new_column)
            #Create the compare_html from the create_compare method in the compare_page instance of the CompareHTML class with the array of columns from the same instance.
            compare_html = compare_page.create_compare(compare_page)
            #Create the page HTML with the compare_page css and html using the create_page method from the pg instance of the Page() class.
            html = pg.create_page(compare_page.css, compare_html)
        #If no GET create the form page
        else:
            #Create an instance of the FormHTML class named form_page
            form_page = FormHTML()
            #Create the form_html from the creat_form method in the form_page instance of the FormHTML class with the array of columns from the same instance.
            form_html = form_page.create_form(products.items)
            #Create the page HTML with the form_page css and html using the create_page method from teh pg instance of the Page() class.
            html = pg.create_page(form_page.css, form_html)
        #Write the HTML to the page.
        self.response.write(html)
#Google Apps launcher setup.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
