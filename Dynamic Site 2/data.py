#Import re for regex.
import re
#Import datetime for date and time calculations
import datetime
#Import the contactLib class from lib to hold the contact information.
from lib import contactLib

#The data class to hold the contacts.
class Data(object):
    #The initilization function.
    def __init__(self):
        #A varaible to hold the contacts
        self.__contacts = ''
        #Make the contacts attribute an instance of the contact library from lib.
        self.contacts = contactLib()
        #Create an instance of the Contact class.
        c1 = Contact()
        #Use the add_contact method to population the information for the contact.
        c1.add_contact("Simeon", "Smith", 15092806173, "smsmith1@fullsail.edu", "Wombat Web Design", "Owner/Designer", "11/15/1988", "07/25/2016")
        #Add the contact to the contacts library using the add_contact function which comes from the contactLib class.
        self.contacts.add_contact(c1)
        #Create an second instance of the Contact class.
        c2 = Contact()
        #Use the add_contact method to population the information for the contact.
        c2.add_contact("James", "Thompson", 13472817543, "tofieldya@gmail.com", "Design Bright", "Web Developer", "02/11/2010", "03/22/2015")
        #Add the contact to the contacts library using the add_contact function which comes from the contactLib class.
        self.contacts.add_contact(c2)
        #Create an thrid instance of the Contact class.
        c3 = Contact()
        #Use the add_contact method to population the information for the contact.
        c3.add_contact("Neesa", "King", 12814273819, "neesa.king@purfectlogos.com", "Purfect Logos", "Screen Printer", "09/02/2011", "12/10/2015")
        #Add the contact to the contacts library using the add_contact function which comes from the contactLib class.
        self.contacts.add_contact(c3)
        #Create an fourth instance of the Contact class.
        c4 = Contact()
        #Use the add_contact method to population the information for the contact.
        c4.add_contact("Daryl", "Perkins", 13247561821, "dperkins@klmfg.com", "K-L Mfg. Co.", "Manager", "08/17/2013", "07/22/2016")
        #Add the contact to the contacts library using the add_contact function which comes from the contactLib class.
        self.contacts.add_contact(c4)
        #Create an fifth instance of the Contact class.
        c5 = Contact()
        #Use the add_contact method to population the information for the contact.
        c5.add_contact("Maria", "Joynes", 12738539238, "maria.joynes@cbnw.com", "Coldwell Banker", "Marketing Director", "04/22/2010", "09/12/2011")
        #Add the contact to the contacts library using the add_contact function which comes from the contactLib class.
        self.contacts.add_contact(c5)

    #The contacts getter
    @property
    def contacts(self):
        return self.__contacts
    #The contacts setter.
    @contacts.setter
    def contacts(self, lib):
        self.__contacts = lib

#Contact class to make the contacts.
class Contact(object):
    #Initilization function
    def __init__(self):
        #Variables to hold the contact information.
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
    #First name getter.
    @property
    def first_name(self):
        return self.__first_name
    #First name setter which checks to make sure the value is a string. Otherwise it returns the error.
    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, basestring):
            self.__first_name = first_name
        else:
            raise ValueError("You entered " + str(first_name) + " for the first name but it is not a valid string.")
    #Last name getter.
    @property
    def last_name(self):
        return self.__last_name
    #Last name setter which checks to make sure the value is a string. Otherwise ti returns the error.
    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, basestring):
            self.__last_name = last_name
        else:
            raise ValueError("You entered " + str(last_name) + " for the last name but it is not a valid string.")
    #Phone number getter which returns the phone number variable as an appropriately formatted string.
    @property
    def phone_number(self):
        phone_number = str(self.__phone_number)
        return phone_number[0] + '.' + phone_number[1:4] + '.' + phone_number[4:7] + '.' + phone_number[7:]
    #Phone Number getter which first checks to see if it is an integer, otherwise it returns a type error, then it checks to see if it's the appropriate 11 characters, otherwise it returns a value error.
    @phone_number.setter
    def phone_number(self, phone_number):
        if isinstance(phone_number, int):
            if len(str(phone_number)) == 11:
                self.__phone_number = phone_number
            else:
                raise ValueError("Your contact " + self.__first_name + " " + self.__last_name + "'s phone number is not the correct length. You entereted " + str(phone_number) + ". Please enter 11 digits.")
        else:
            raise TypeError("Your contact " + self.__first_name + " " + self.__last_name + "'s phone number is not a number. You entered " + str(phone_number) + ". Please enter only numbers.")
    #Email getter.
    @property
    def email(self):
        return self.__email
    #Email setter which first checks to see if the value is a string, otherwise it returns a type error, then it checks to see if it matches the regex for emails, otherwise it returns a value errro.
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
    #Company getter.
    @property
    def company(self):
        return self.__company
    #Company setter which checks to see fi the value is a string, otherwise it returns an error.
    @company.setter
    def company(self, company):
        if isinstance(company, basestring):
            self.__company = company
        else:
            raise ValueError("Your contact " + self.__first_name + " " + self.__last_name + "'s company is not a string. You entered " + str(company) + " for the company. Please enter only a string.")
    #Title getter.
    @property
    def title(self):
        return self.__title
    #Title setter which checks to see fi the value is a string, otherwise it returns an error.
    @title.setter
    def title(self, title):
        if isinstance(title, basestring):
            self.__title = title
        else:
            raise ValueError("Your contact " + self.__first_name + " " + self.__last_name + "'s title is not a string. You entered " + str(title) + " for the title. Please enter only a string.")
    #First contact getter.
    @property
    def first_contact(self):
        return self.__first_contact
    #First contact setter which first checks to see if the value is a string, othwise it returns a type error. Then it checks to see if it matchs the appropriate regex format for the date, otherwise it returns a value errro.
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
    #Know for setter which sets the __know_for variable to the number of years this contact has been known.
    @property
    def known_for(self):
        first_contact = self.first_contact.split('/')
        current_year = datetime.datetime.today().year
        self.__known_for = current_year - int(first_contact[2])
        return self.__known_for
    #Last contact getter
    @property
    def last_contact(self):
        return self.__last_contact
    #Last contact setter which first checks to see if the value is a string, othwise it returns a type error. Then it checks to see if it matchs the appropriate regex format for the date, otherwise it returns a value errro.
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
    #Months past contact getter
    @property
    def months_past_contact(self):
        return self.__months_past_contact
    #Needs contact getter
    @property
    def needs_contact(self):
        return self.__needs_contact
    #The add contact function which uses the passed in varaibles to setup the contact.
    def add_contact(self, first_name, last_name, phone_number, email, company, title, first_contact, last_contact):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.company = company
        self.title = title
        self.first_contact = first_contact
        self.last_contact = last_contact

        #Current year, month and date for calculations below.
        current_year = datetime.datetime.today().year
        current_day = datetime.datetime.today().day
        current_month = datetime.datetime.today().month
        #Last contact date split at the /
        last_contact = last_contact.split('/')
        #If the last contact year is less than the current year.
        if int(last_contact[2]) < current_year:
            #The check if the it's been more than a year since last contact.
            if (current_year - int(last_contact[2])) > 1:
                #If yes then set the months past contact to 12 and needs contact to true.
                self.__months_past_contact = 12
                self.__needs_contact = True
            #Othwerise check to see how many months past contact it has been.
            else:
                #Calculate the months past contact.
                self.__months_past_contact = (12 - int(last_contact[0])) + current_month - 1
                #If greater or equal to 3 months then set needs contact to true.
                if self.__months_past_contact >=3:
                    self.__needs_contact = True
                #Otherwise set to false.
                else:
                    self.__needs_contact = False
        #Else if the last contact year is the same as the current year.
        elif int(last_contact[2]) == current_year:
            #Calculate the months past contact.
            self.__months_past_contact = current_month - int(last_contact[0])
            #If greater or equal to 3 months then set needs contact to true.
            if self.__months_past_contact >=3:
                self.__needs_contact = True
            #Otherwise set to false.
            else:
                self.__needs_contact = False