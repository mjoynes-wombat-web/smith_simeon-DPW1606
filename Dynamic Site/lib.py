#The Contact Library class to hold the contacts. Used in the data.py file.
class contactLib(object):
    #Initilization function.
    def __init__(self):
        #An array to hold the contacts.
        self.__list = []
    #The getter for the contacts list.
    @property
    def list(self):
        return self.__list
    #A function to add the contacts to the list.
    def add_contact(self, contact):
        #Append the contact to the list array.
        self.__list.append(contact)