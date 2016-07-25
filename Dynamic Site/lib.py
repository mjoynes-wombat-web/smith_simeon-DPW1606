class contactLib(object):
    def __init__(self):
        self.__list = []

    @property
    def list(self):
        return self.__list

    def add_contact(self, contact):
        self.__list.append(contact)