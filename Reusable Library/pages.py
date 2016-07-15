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
    <title>Business Card Creator</title>
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
            <h2>Enter Products Here</h2>
            <form>
                <fieldset>
                    <label for="pName">Name:</label>
                    <input type="text" name="pName" id="pName" placeholder="Macorni and Cheese" required >
                </fieldset>
                <fieldset>
                    <label for="pBrand">Brand:</label>
                    <input type="text" name="pBrand" id="pName" placeholder="Kraft">
                </fieldset>
                <fieldset>
                    <label for="pPrice">Price:</label>
                    <input type="text" name="pPrice" id="pPrice" placeholder="12.50" required pattern="^[+-]?[0-9]{{1,3}}(?:,?[0-9]{{3}})*(?:\.[0-9]{{2}})?$" oninvalid="this.setCustomValidity('This is not a valid number. Please enter only a number. ie 1.57.')" oninput="setCustomValidity('')">
                </fieldset>
                <fieldset>
                    <label for="pWeight">Weight:</label>
                    <input type="text" name="pWeight" id="pWeight" placeholder="14" required pattern="[0-9]+" oninvalid="this.setCustomValidity('This is not a valid number. Please enter only a number.')" oninput="setCustomValidity('')">
                    <select name="pUnit" required>
                        <option value="" disabled selected>Unit</option>
                        <option value="oz">oz.</option>
                        <option value="lb">lbs.</option>
                    </select>
                </fieldset>
                <input type="text" name="form" value="addProduct" style="display:none">
                <input type="submit" value="Add to Compare">
            </form>
        </section>
        <section>
            <h2>Products to Compare</h2>
            <p>1/5 : Your products will automatically be compared once you reach 5.</p>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Brand</th>
                    <th>Price</th>
                    <th>Weight</th>
                </tr>
                {product_rows}
            </table>
            <form>
                <input type="text" name="form" value="compare" style="display:none">
                <input type="submit" value="Compare Products">
            </form>
        </section>
    </main>
        '''
        self.__product_rows = ''
        self.__product_row = '''
                <tr>
                    <td>{product.name}</td>
                    <td>{product.brand}</td>
                    <td>{product.price}</td>
                    <td>{product.weight}</td>
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

        print product_rows
        page_html = self.__main
        
        return page_html.format(**locals())
