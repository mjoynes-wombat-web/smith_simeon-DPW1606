import re
import datetime
from lib import contactLib

class Data(object):
    def __init__(self):
        self.__contacts = ''

        @property
        def contacts(self):
            return self.__contacts

        @contacts.setter
        def contacts(self, lib):
            self.__contacts = lib

class DataMultiObject(Data):
    def __init__(self):
        Data.__init__(self)
        
        self.contacts = contactLib()

        c1 = Contact()
        c1.add_contact("Simeon", "Smith", 15092806173, "smsmith1@fullsail.edu", "Wombat Web Design", "Owner/Designer", "11/15/1988", "07/25/2016")
        self.contacts.add_contact(c1)

        c2 = Contact()
        c2.add_contact("James", "Thompson", 13472817543, "tofieldya@gmail.com", "Design Bright", "Web Developer", "02/11/2010", "03/22/2015")
        self.contacts.add_contact(c2)

        c3 = Contact()
        c3.add_contact("Neesa", "King", 12814273819, "neesa.king@purfectlogos.com", "Purfect Logos", "Screen Printer", "09/02/2011", "12/10/2015")
        self.contacts.add_contact(c3)

        c4 = Contact()
        c4.add_contact("Daryl", "Perkins", 13247561821, "dperkins@klmfg.com", "K-L Mfg. Co.", "Manager", "08/17/2013", "07/22/2016")
        self.contacts.add_contact(c4)

        c5 = Contact()
        c5.add_contact("Maria", "Joynes", 12738539238, "maria.joynes@cbnw.com", "Coldwell Banker", "Marketing Director", "04/22/2010", "09/12/2011")
        self.contacts.add_contact(c5)

class DataMultiClass(Data):
    def __init__(self):
        Data.__init__(self)

        self.contacts = contactLib()

        c1 = ssmithContact()
        self.contacts.add_contact(c1)

        c2 = jthompsonContact()
        self.contacts.add_contact(c2)

        c3 = nkingContact()
        self.contacts.add_contact(c3)

        c4 = dperkinsContact()
        self.contacts.add_contact(c4)

        c5 = mjoynesContact()
        self.contacts.add_contact(c5)

class Contact(object):
    def __init__(self):
        self.__first_name = ''
        self.__last_name = ''
        self.__phone_number = 0
        self.__email = ''
        self.__company = ''
        self.__title = ''
        self.__first_contact = ''
        self.__last_contact = ''
        self.__months_past_contact = 0
        self.__needs_contact = False
        self.__known_for = ''

    @property
    def known_for(self):
        first_contact = self.first_contact.split('/')
        current_year = datetime.datetime.today().year
        self.__known_for = current_year - int(first_contact[2])
        return self.__known_for

    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, basestring):
            self.__first_name = first_name
        else:
            raise ValueError("You entered " + str(first_name) + " for the first name but it is not a valid string.")

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, basestring):
            self.__last_name = last_name
        else:
            raise ValueError("You entered " + str(last_name) + " for the last name but it is not a valid string.")

    @property
    def phone_number(self):
        phone_number = str(self.__phone_number)
        return phone_number[0] + '.' + phone_number[1:4] + '.' + phone_number[4:7] + '.' + phone_number[7:]
    @phone_number.setter
    def phone_number(self, phone_number):
        if isinstance(phone_number, int):
            if len(str(phone_number)) == 11:
                self.__phone_number = phone_number
            else:
                raise ValueError("Your contact " + self.__first_name + " " + self.__last_name + "'s phone number is not the correct length. You entereted " + str(phone_number) + ". Please enter 11 digits.")
        else:
            raise TypeError("Your contact " + self.__first_name + " " + self.__last_name + "'s phone number is not a number. You entered " + str(phone_number) + ". Please enter only numbers.")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        pattern = re.compile("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
        if isinstance(email, basestring):
            if pattern.match(email):
                self.__email = email
            else: 
                raise ValueError("Your contact " + self.__first_name + " " + self.__last_name + "'s email does not mat the approved format. You entered " + str(email) + " for the email. Please enter a valid email.")
        else:
            raise TypeError("Your contact " + self.__first_name + " " + self.__last_name + "'s email is not a string. You entered " + str(email) + " for the email. Please enter only a string.")

    @property
    def company(self):
        return self.__company
    @company.setter
    def company(self, company):
        if isinstance(company, basestring):
            self.__company = company
        else:
            raise ValueError("Your contact " + self.__first_name + " " + self.__last_name + "'s company is not a string. You entered " + str(company) + " for the company. Please enter only a string.")

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title):
        if isinstance(title, basestring):
            self.__title = title
        else:
            raise ValueError("Your contact " + self.__first_name + " " + self.__last_name + "'s title is not a string. You entered " + str(title) + " for the title. Please enter only a string.")
    
    @property
    def first_contact(self):
        return self.__first_contact
    @first_contact.setter
    def first_contact(self, first_contact):
        pattern = re.compile("[0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9]")
        if isinstance(first_contact, basestring):
            if pattern.match(first_contact):
                self.__first_contact = first_contact
            else:
                raise ValueError("Your contact " + self.__first_name + " " + self.__last_name + "'s first contact date does not match the approved format. You entered " + str(first_contact) + " for the first contact date. Please enter a date in this format MM/DD/YYYY")
        else:
            raise TypeError("Your contact " + self.__first_name + " " + self.__last_name + "'s first contact date is not a string. You entered " + str(first_contact) + " for first contact date. Please enter only a string.")

    @property
    def last_contact(self):
        return self.__last_contact
    @last_contact.setter
    def last_contact(self, last_contact):
        pattern = re.compile("[0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9]")
        if isinstance(last_contact, basestring):
            if pattern.match(last_contact):
                self.__last_contact = last_contact
            else:
                raise ValueError("Your contact " + self.__first_name + " " + self.__last_name + "'s last contact date does not match the approved format. You entered " + str(last_contact) + " for the last contact date. Please enter a date in this format MM/DD/YYYY")
        else:
            raise TypeError("Your contact " + self.__first_name + " " + self.__last_name + "'s last contact date is not a string. You entered " + st(last_contact) + " for last contact date. Please enter only a string.")

    @property
    def months_past_contact(self):
        return self.__months_past_contact
    @property
    def needs_contact(self):
        return self.__needs_contact

    def add_contact(self, first_name, last_name, phone_number, email, company, title, first_contact, last_contact):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.company = company
        self.title = title
        self.first_contact = first_contact
        self.last_contact = last_contact

        current_year = datetime.datetime.today().year
        current_day = datetime.datetime.today().day
        current_month = datetime.datetime.today().month
        first_contact = first_contact.split('/')
        last_contact = last_contact.split('/')

        if int(last_contact[2]) < current_year:
            if (int(last_contact[2]) - current_year) > 1:
                self.__months_past_contact = 12
                self.__needs_contact = True
            else:
                self.__months_past_contact = (12 - int(last_contact[0])) + current_month - 1
                if self.__months_past_contact >=3:
                    self.__needs_contact = True
                else:
                    self.__needs_contact = False
        elif int(last_contact[2]) == current_year:
            self.__months_past_contact = current_month - int(last_contact[0])
            if self.__months_past_contact >=3:
                self.__needs_contact = True
            else:
                self.__needs_contact = False

class ssmithContact(Contact):
    def __init__(self):
        Contact.__init__(self)

        self.add_contact("Simeon", "Smith", 15092806173, "smsmith1@fullsail.edu", "Wombat Web Design", "Owner/Designer", "11/15/1988", "07/25/2016")

class jthompsonContact(Contact):
    def __init__(self):
        Contact.__init__(self)

        self.add_contact("James", "Thompson", 13472817543, "tofieldya@gmail.com", "Design Bright", "Web Developer", "02/11/2010", "03/22/2015")

class nkingContact(Contact):
    def __init__(self):
        Contact.__init__(self)

        self.add_contact("Neesa", "King", 12814273819, "neesa.king@purfectlogos.com", "Purfect Logos", "Screen Printer", "09/02/2011", "12/10/2015")

class dperkinsContact(Contact):
    def __init__(self):
        Contact.__init__(self)

        self.add_contact("Daryl", "Perkins", 13247561821, "dperkins@klmfg.com", "K-L Mfg. Co.", "Manager", "08/17/2013", "07/22/2016")

class mjoynesContact(Contact):
    def __init__(self):
        Contact.__init__(self)

        self.add_contact("Maria", "Joynes", 12738539238, "maria.joynes@cbnw.com", "Coldwell Banker", "Marketing Director", "04/22/2010", "09/12/2011")