class Page(object):
    def __init__(self):
        self.__html_temp = '''
<!DOCTYPE html>
<html lang="en">
{head}
{body}
</html>
        '''
        self.__head_temp = '''
<head>
    <title>ShopEZ - Grocery Price Comparison Tool</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="css/style.css" >
    <link href="https://fonts.googleapis.com/css?family=Copse|Roboto:100,300,400" rel="stylesheet">
    {page_css}
</head>
        '''
        self.__body_temp = '''
<body>
    {header}
    {main}
</body>
        '''
        self.__header_temp = '''
    <header>
        <h1>ShopEZ</h1>
        <p>Grocery Price Comparison Tool</p>
    </header>
        '''

    def create_page(self, page_css, main):
        page_html = self.__html_temp
        head = self.__head_temp
        header = self.__header_temp
        body = self.__body_temp

        head = head.format(**locals())
        body = body.format(**locals())
        page_html = page_html.format(**locals())

        return page_html



class Form(object):
    def __init__(self):
        self.__css = '''<link href="css/form.css" rel="stylesheet"/>'''

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
        self.__product_rows = ''
        self.__product_row = '''
                <tr>
                    <td>{product.name}</td>
                    <td>{product.brand}</td>
                    <td>{product.price_text}</td>
                    <td>{product.weight_text}</td>
                </tr>
        '''

    @property
    def css(self):
        return self.__css

    def add_product_row(self, product):
        return self.__product_row.format(**locals())

    def create_form(self, products):
        for product in products:
            self.__product_rows += self.add_product_row(product)

        product_rows = self.__product_rows

        page_html = self.__main
        
        return page_html.format(**locals())
        
