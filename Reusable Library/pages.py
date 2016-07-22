#A class for the main page elements of the application.
class Page(object):
    #The initilization function, which holds the variables for use.
    def __init__(self):
        #Main html template with a placehodler or the head and body.
        self.__html_temp = '''
<!DOCTYPE html>
<html lang="en">
{head}
{body}
</html>'''
        #Head html template with a placeholder for the page specific CSS.
        self.__head_temp = '''
<head>
    <title>ShopEZ - Grocery Price Comparison Tool</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="css/style.css" >
    {page_css}
    <link href="https://fonts.googleapis.com/css?family=Copse|Roboto:100,300,400" rel="stylesheet">
</head>'''
        #Body html template with a placeholder for the header and main content.
        self.__body_temp = '''
<body>
    {header}
    {main}
</body>'''
        #Header html template
        self.__header_temp = '''
    <header>
        <h1>ShopEZ</h1>
        <p>Grocery Price Comparison Tool</p>
    </header>'''
    #A fucntion for creating the page with passed in page_css and main html
    def create_page(self, page_css, main):
        page_html = self.__html_temp                #Making the html_temp variable a local variable for use in formatting.
        head = self.__head_temp                     #Making the head_temp variable a local variable for use in formatting.
        header = self.__header_temp                 #Making the header_temp variable a local variable for use in formatting.
        body = self.__body_temp                     #Making the body_temp variable a local variable for use in formatting.

        head = head.format(**locals())              #Format the head using the local page_css variable
        body = body.format(**locals())              #Format the body using the local header and main variables
        page_html = page_html.format(**locals())    #Format the page html using the local head and body varaibles

        return page_html                            #Return the page html.
#A class for the form page elements of the application.
class FormHTML(object):
    #The initilization funciton, which holds the variables for use.
    def __init__(self):
        #Form css tag.
        self.__css = '''<link href="css/form.css" rel="stylesheet"/>'''
        #Form main html content with the product_rows placeholder.
        self.__main = '''
    <main>
        <section>
            <h2>Products to Compare</h2>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Brand</th>
                    <th>Price</th>
                    <th>Weight</th>
                </tr>
                {product_rows}
            </table>
        </section>
        <section>
            <h2>Enter Products Here</h2>
            <form>
                <fieldset>
                    <label for="pName">Name:</label>
                    <input type="text" name="pName" id="pName" placeholder="Shells and Cheddar" required >
                </fieldset>
                <fieldset>
                    <label for="pBrand">Brand:</label>
                    <input type="text" name="pBrand" id="pName" placeholder="Kirkland">
                </fieldset>
                <fieldset>
                    <label for="pPrice">Price:</label>
                    <input type="text" name="pPrice" id="pPrice" placeholder="18.00" required pattern="^[+-]?[0-9]{{1,3}}(?:,?[0-9]{{3}})*(?:\.[0-9]{{2}})?$" oninvalid="this.setCustomValidity('This is not a valid number. Please enter only a number. ie 1.57.')" oninput="setCustomValidity('')">
                </fieldset>
                <fieldset>
                    <label for="pWeight">Weight:</label>
                    <input type="text" name="pWeight" id="pWeight" placeholder="12" required pattern="[0-9]+" oninvalid="this.setCustomValidity('This is not a valid number. Please enter only a number.')" oninput="setCustomValidity('')">
                    <select name="pUnit" required>
                        <option value="" disabled selected>Unit</option>
                        <option value="oz">oz.</option>
                        <option value="lb">lbs.</option>
                    </select>
                </fieldset>
                <input type="submit" value="Add & Compare">
            </form>
        </section>
    </main>
        '''
        #A variable to hold the string of product rows.
        self.__product_rows = ''
        #The product rows template with placeholders.
        self.__product_row = '''
                <tr>
                    <td>{product.name}</td>
                    <td>{product.brand}</td>
                    <td>{product.price_text}</td>
                    <td>{product.weight_text}</td>
                </tr>
        '''
    #Getter for the css.
    @property
    def css(self):
        return self.__css
    #A function that creates a prodcut row from the variable above.
    def add_product_row(self, product):
        return self.__product_row.format(**locals())
    #A function for creating the form content, looking through the products passed in to create the product rows and fomatting the placeholders.
    def create_form(self, products):
        for product in products:
            self.__product_rows += self.add_product_row(product)

        product_rows = self.__product_rows
        
        return self.__main.format(**locals())
#A class for the compare page elements of the application.
class CompareHTML(object):
    #The initilization function which holds the variables for use.
    def __init__(self):
        #Compare page css tag.
        self.__css = '''<link rel="stylesheet" href="css/compare.css"/>'''
        #Compare page main content.
        self.__main = '''
    <main>
        <section>
            <h2>Price Per Ounce Comparison</h2>
            <table>
                <tr>
                    <th>Price Per Ounce</th>
                    {compare_columns.price_ounce}
                </tr>
                <tr>
                    <th>Name</th>
                    {compare_columns.name}
                </tr>
                <tr>
                    <th>Brand</th>
                    {compare_columns.brand}
                </tr>
                <tr>
                    <th>Price</th>
                    {compare_columns.price}
                </tr>
                <tr>
                    <th>Weight</th>
                    {compare_columns.weight}
                </tr>
            </table>
        </section>
    </main>
        '''
        #Variables to hold the various product column's html.
        self.__price_ounce = ''
        self.__name = ''
        self.__brand = ''
        self.__price = ''
        self.__weight = ''
    #CSS Getter
    @property
    def css(self):
        return self.__css
    #Price per ounce Getter
    @property
    def price_ounce(self):
        return self.__price_ounce
    #Name Getter
    @property
    def name(self):
        return self.__name
    #Brand Getter
    @property
    def brand(self):
        return self.__brand
    #Price Getter
    @property
    def price(self):
        return self.__price
    #Weight Getter
    @property
    def weight(self):
        return self.__weight
    #A function which takes the new column variables and adds them to the appropriate column string.
    def add_product_column(self, new_column):
        self.__price_ounce += new_column.ounce_price_row
        self.__name += new_column.name_row
        self.__brand += new_column.brand_row
        self.__price += new_column.price_row
        self.__weight += new_column.weight_row
    #A function which returns the formatted html for the compare page.
    def create_compare(self, compare_columns):
        return self.__main.format(**locals())
#A class for the individual compare columns
class compareColumn(object):
    #The initilization function which holds the variables for use.
    def __init__(self):
        #Variables for the row templates.
        self.__ounce_price_row = '''
                    <td>{product.cost_oz_text}</td>
        '''
        self.__name_row = '''
                    <td>{product.name}</td>
        '''
        self.__brand_row = '''
                    <td>{product.brand}</td>
        '''
        self.__price_row = '''
                    <td>{product.price_text}</td>
        '''
        self.__weight_row = '''
                    <td>{product.weight_text}</td>
        '''
    #Price Per Ounce Row Getter
    @property
    def ounce_price_row(self):
        return self.__ounce_price_row
    #Price Per Ounce Row Setter which creates the td based on the passed in variables.
    @ounce_price_row.setter
    def ounce_price_row(self, product):
        self.__ounce_price_row = self.__ounce_price_row.format(**locals())
    #Name Row Getter
    @property
    def name_row(self):
        return self.__name_row
    #Name Row Setter which creates the td based on the passed in variables.
    @name_row.setter
    def name_row(self, product):
        self.__name_row = self.__name_row.format(**locals())
    #Brand Row Getter
    @property
    def brand_row(self):
        return self.__brand_row
    #Brand Row Setter which creates the td based on the passed in variables.
    @brand_row.setter
    def brand_row(self, product):
        self.__brand_row = self.__brand_row.format(**locals())
    #Price Row Getter
    @property
    def price_row(self):
        return self.__price_row
    #Price Row Setter which creates the td based on the passed in variables.
    @price_row.setter
    def price_row(self, product):
        self.__price_row = self.__price_row.format(**locals())
    #Weight Row Getter
    @property
    def weight_row(self):
        return self.__weight_row
    #Weight Row Setter which creates the td based on the passed in variables.
    @weight_row.setter
    def weight_row(self, product):
        self.__weight_row = self.__weight_row.format(**locals())
    #A function that creates each row of the columns based on the passed in product variable.
    def create_column(self, product):
        self.ounce_price_row = product
        self.name_row = product
        self.brand_row = product
        self.price_row = product
        self.weight_row = product
