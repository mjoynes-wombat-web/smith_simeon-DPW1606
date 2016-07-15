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
        return "$" + str(self.__price)

    @price.setter
    def price(self, p_price):
        self.__price = p_price

    @property
    def weight(self):
        return str(self.__weight) + ' ' + self.__weight_unit

    @weight.setter
    def weight(self, p_weight):
        self.__weight = p_weight

    @property
    def weight_unit(self):
        pass

    @weight_unit.setter
    def weight_unit(self, p_weight_unit):
        self.__weight_unit = p_weight_unit