class Product(object):
    def __init__(self):
        self.__name = ''
        self.__brand = ''
        self.__price = ''
        self.__weight = 0
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

    @property
    def price_text(self):
        return "$" + str(format(self.__price, '.2f'))

    @price.setter
    def price(self, p_price):
        self.__price = float(p_price)

    @property
    def weight(self):
        return self.__weight
    
    @property
    def weight_text(self):
        return str(self.__weight) + ' ' + self.__weight_unit

    @weight.setter
    def weight(self, p_weight):
        self.__weight = float(p_weight)

    @property
    def weight_unit(self):
        return self.__weight_unit

    @weight_unit.setter
    def weight_unit(self, p_weight_unit):
        self.__weight_unit = p_weight_unit

class CalcCompare(object):
    def __init__(self):
        self.__cost_oz = 0

    @property
    def cost_oz(self):
        return self.__cost_oz

    def calc_cost_oz(self, price, weight, weight_unit):
        if weight_unit == "oz":
            self.__cost_oz = price / weight
        elif weight_unit == "lb":
            self.__cost_oz = price / (weight * 16)
        else:
            print "Invalid unit of measurement."

        return round(self.__cost_oz, 2)