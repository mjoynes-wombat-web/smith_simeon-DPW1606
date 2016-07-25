class Contact(object):
    def __init__(self):
        self.__first_name = ''
        self.__last_name = ''
        self.__phone_number = 0
        self.__company = ''
        self.__title = ''
        self.__first_contact = ''
        self.__last_contact = ''

    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, basestring):
            self.__first_name = first_name
        else:
            print first_name + " for first name defined is not a valid string."

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, basestring):
            self.__last_name = last_name
        else:
            print last_name + " for last name defined is not a valid string."

    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self, phone_number):
        if isinstance(phone_number, int):
            if len(str(phone_number)) == 11:
                self.__phone_number = phone_number
            else:
                print str(phone_number) + " for phone number isn't the correct length. Please enter 11 digits.'"
        else:
            print str(phone_number) + " for phone number can only be set to a number. Please enter only numbers"

    @property
    def company(self):
        return self.__company
    @company.setter
    def company(self, company):
        if isinstance(company, basestring):
            self.__company = company
        else:
            print company + " for company is not a valid string."

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title):
        if isinstance(title, basestring):
            self.__title = title
        else:
            print title + " for title is not a valid string."
    
    @property
    def first_contact(self):
        return self.__first_contact
    @first_contact.setter
    def first_contact(self, first_contact):
        if isinstance(first_contact, basestring):
            self.__first_contact = first_contact
        else:
            print first_contact + " for first contact is not a valid string"

    @property
    def last_contact(self):
        return self.__last_contact
    @last_contact.setter
    def last_contact(self, last_contact):
        if isinstance(last_contact, basestring):
            self.__last_contact = last_contact
        else:
            print last_contact + " for last contact is not a valid string"

    def add_contact(self, first_name, last_name, phone_number, company, title, first_contact, last_contact):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.company = company
        self.title = title
        self.first_contact = first_contact
        self.last_contact = last_contact

c1 = Contact()
c1.add_contact("Simeon", "Smith", 5092806173, "Wombat Web Design", "Owner/Designer", "11/15/88", "07/25/16")
