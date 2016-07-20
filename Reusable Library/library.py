class productData(object):
    def __init__(self):
        self.__items = []

    def add_to_array(self, product):
        self.__items.append(product)

    @property
    def items(self):
        return self.__items

class Product(object):
    def __init__(self):
        self.__name = ''
        self.__brand = ''
        self.__price = ''
        self.__price_text = ''
        self.__weight = 0
        self.__weight_text = ''
        self.__weight_unit = ''
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, p_name):
        self.__name = p_name

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, p_brand):
        self.__brand = p_brand

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, p_price):
        self.__price = float(p_price)

    @property
    def price_text(self):
        self.__price_text = self.concat_price_text()
        return self.__price_text

    def concat_price_text(self):
        return "$" + str(format(self.__price, '.2f'))

    @price_text.setter
    def price_text(self):
        pass

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, p_weight):
        self.__weight = float(p_weight)

    @property
    def weight_text(self):
        self.__weight_text = self.concat_weight_text()
        return self.__weight_text

    def concat_weight_text(self):
        return str(self.__weight) + ' ' + self.__weight_unit

    @weight_text.setter
    def weight_text(self):
        pass

    @property
    def weight_unit(self):
        return self.__weight_unit

    @weight_unit.setter
    def weight_unit(self, p_weight_unit):
        self.__weight_unit = p_weight_unit

    def add_product(self, name, brand, price, weight, weight_unit):
        self.name = name
        self.brand = brand
        self.price = price
        self.weight = weight
        self.weight_unit = weight_unit

class CompareProduct(Product):
    def __init__(self):
        Product.__init__(self)
        self.__cost_oz = 0
        self.__cost_oz_text = ''

    @property
    def cost_oz(self):
        return self.__cost_oz

    def concat_cost_oz_text(self):
        return "$" + str(format(self.__cost_oz, '.2f'))

    @property
    def cost_oz_text(self):
        self.__cost_oz_text = self.concat_cost_oz_text()
        return self.__cost_oz_text

    def calc_cost_oz(self):
        if self.weight_unit == "oz":
            cost_oz = self.price / self.weight
        elif self.weight_unit == "lb":
            cost_oz = self.price / (self.weight * 16)
        else:
            print "Invalid unit of measurement."

        self.__cost_oz = round(cost_oz, 2)

    def import_products(self, product):
        pass

    def add_product(self, name, brand, price, weight, weight_unit):
        self.name = name
        self.brand = brand
        self.price = price
        self.weight = weight
        self.weight_unit = weight_unit
        self.calc_cost_oz()