#A class to hold the product data.
class productData(object):
    #Init function storing the items array which holds the product data.
    def __init__(self):
        self.__items = []
    #Function to add product to the array.
    def add_to_array(self, product):
        self.__items.append(product)
    #The getter for the items array.
    @property
    def items(self):
        return self.__items
#A class for the products.
class Product(object):
    #The init function which holds the variables for the product.
    def __init__(self):
        self.__name = ''
        self.__brand = ''
        self.__price = ''
        self.__price_text = ''
        self.__weight = 0
        self.__weight_text = ''
        self.__weight_unit = ''
    #The getter for the name attribute.
    @property
    def name(self):
        return self.__name
    #The setter for the name attribute.
    @name.setter
    def name(self, p_name):
        self.__name = p_name
    #The getter for the brand attribute.
    @property
    def brand(self):
        return self.__brand
    #The setter for the brand attribute.
    @brand.setter
    def brand(self, p_brand):
        self.__brand = p_brand
    #The getter for the price.
    @property
    def price(self):
        return self.__price
    #The setter for the price which converts whatever is passed in into a floating number.
    @price.setter
    def price(self, p_price):
        self.__price = float(p_price)
    #The getter for the price text which formats the price with the concat_price_text function.
    @property
    def price_text(self):
        self.__price_text = self.concat_price_text()
        return self.__price_text
    #A function, used above, to format the price making it appropriate for display.
    def concat_price_text(self):
        return "$" + str(format(self.__price, '.2f'))
    #The getter for the weight.
    @property
    def weight(self):
        return self.__weight
    #The setter for the weight.
    @weight.setter
    def weight(self, p_weight):
        self.__weight = float(p_weight)
    #The getter for the weight text which formats the price with the concat_weight_text function.
    @property
    def weight_text(self):
        self.__weight_text = self.concat_weight_text()
        return self.__weight_text
    #The concat_concat_weight function which returns the weight and weight unit varaible appropirately for display.
    def concat_weight_text(self):
        return str(self.__weight) + ' ' + self.__weight_unit
    #The getter for the weight unit.
    @property
    def weight_unit(self):
        return self.__weight_unit
    #The setter for the weight unit.
    @weight_unit.setter
    def weight_unit(self, p_weight_unit):
        self.__weight_unit = p_weight_unit
    #A function to which the product attributes can be passed and sets all the values.
    def add_product(self, name, brand, price, weight, weight_unit):
        self.name = name
        self.brand = brand
        self.price = price
        self.weight = weight
        self.weight_unit = weight_unit
#The compare product class which is a subclass of the Product class.
class CompareProduct(Product):
    #The init function which pulls in the information from the Product class and adds two attributes for the cost per ounce.
    def __init__(self):
        Product.__init__(self)
        self.__cost_oz = 0
        self.__cost_oz_text = ''
    #The getter for the cost_oz.
    @property
    def cost_oz(self):
        return self.__cost_oz
    #A function to format the cost per ounce appropiately for display.
    def concat_cost_oz_text(self):
        return "$" + str(format(self.__cost_oz, '.2f'))
    #The cost per ounce text getter which sets the cost per ounce with the function above for formatting and returns the variable.
    @property
    def cost_oz_text(self):
        self.__cost_oz_text = self.concat_cost_oz_text()
        return self.__cost_oz_text
    #The calc cost per ounce function which is used to calculate the cost per ounce.
    def calc_cost_oz(self):
        #If the weight unit is set to ounces set the local cost_oz to the following calculation.
        if self.weight_unit == "oz":
            cost_oz = self.price / self.weight
        #Else if the weight unit is set to pounts set the local cost_oz to the following calculation.
        elif self.weight_unit == "lb":
            cost_oz = self.price / (self.weight * 16)
        #Else return erro message.
        else:
            print "Invalid unit of measurement."
        #Set the __cost_oz variable to the cost_oz rounded to 2 decimals.
        self.__cost_oz = round(cost_oz, 2)
    #The add_product function polymorphed to add in the calc_cost_oz function.
    def add_product(self, name, brand, price, weight, weight_unit):
        self.name = name
        self.brand = brand
        self.price = price
        self.weight = weight
        self.weight_unit = weight_unit
        self.calc_cost_oz()