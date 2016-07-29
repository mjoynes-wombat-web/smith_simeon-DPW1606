#Genearal Page class
class Page(object):
#MAIN HTML VARIABLES
    #Initilization function
    def __init__(self):
        #Main html template.
        self.__html_temp = '''
<!DOCTYPE html>
<html lang="en">
{self.head}
{self.body}
</html>'''
        #Variable to contain the formatted html.
        self.__html = ''

#HEAD VARIABLES
        #Head tempalte.
        self.__head_temp = '''
<head>
    <title>{self.title}</title>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css?family=Arima+Madurai:800|Lato:300,400" rel="stylesheet">
    <link href="css/{self.css}" rel="stylesheet">
</head>'''
        #Varaible to hold the formatted head.
        self.__head = ''
        #Variable to hold the title.
        self.__title = ''
        #Variable to hold the css.
        self.__css = ''

#BODY VARIABLES
        #Body template
        self.__body_temp = '''
<body>
    {self.header}
    {self.main}
</body>
        '''
        #Variable to hold the formatted body.
        self.__body = ''
        #Header tempalte
        #HEADER VARIABLES
        self.__header_temp = '''
        <header>
            <h1><a href="/">{self.h1}</a></h1>
        </header>'''
        #Variable to containt formatted header
        self.__header = ''
        #Main content template
        #Variable to hold the h1 text.
        self.__h1 = ''
        #MAIN VARIABLES
        self.__main_temp = '''
        <main>
            {self.main_content}
        </main>'''
        #Variable to contain formatted main section.
        self.__main = ''
        #Variable to contain formatted main content
        self.__main_content = ''

    #HTML getter which formats the html template with the locals
    @property
    def html(self):
        self.__html = self.__html_temp.format(**locals())
        return self.__html
#HEAD VARIABLES GETTERS AND SETTERS
    #Head getter which formats the head template with the locals
    @property
    def head(self):
        self.__head = self.__head_temp.format(**locals())
        return self.__head
    #Title getter
    @property
    def title(self):
        return self.__title
    #Title setter
    @title.setter
    def title(self, title):
        self.__title = title
    #CSS getter
    @property
    def css(self):
        return self.__css
    #CSS setter
    @css.setter
    def css(self, css):
        self.__css = css
#BODY VARIABLES GETTERS AND SETTERS
    #Body getter which formats the body template with the locals
    @property
    def body(self):
        self.__body = self.__body_temp.format(**locals())
        return self.__body
    #Header getter which formats the header template with the locals
    @property
    def header(self):
        self.__header = self.__header_temp.format(**locals())
        return self.__header
    #H1 getter
    @property
    def h1(self):
        return self.__h1
    #H1 setter
    @h1.setter
    def h1(self, h1):
        self.__h1 = h1
    #Main getter whcih formats the main template with the locals
    @property
    def main(self):
        self.__main = self.__main_temp.format(**locals())
        return self.__main
    #Main content getter.
    @property
    def main_content(self):
        return self.__main_content
    #Main content setter.
    @main_content.setter
    def main_content(self, main_content):
        self.__main_content = main_content

#A main page class for the home page which inherits from the Page class.
class mainPage(Page):
    #Initilization function.
    def __init__(self):
        #Run the init for the page class.
        Page.__init__(self)
        #A template for the contact list.
        self.__contact_list_temp = '''
            <nav>
                <ul>
                    {self.contacts}
                </ul>
            </nav>'''
        #A variable to hold the formatted contact list template.
        self.__contact_list = ''
        #A tempalte for the individual contacts. The URL is based on the passed in first_name and last_name when this is formatted
        self.__contact_temp = '''
                    <li><a href="?contact_name={first_name}+{last_name}">{first_name} {last_name}</a></li>'''
        #A variable to hold the concatinated contact list items from the contact template.
        self.__contacts = ''
    #The concatinated contacts getter.
    @property
    def contacts(self):
        return self.__contacts
    #The contact list HTML getter which is formatted with the locals.
    @property
    def contact_list(self):
        self.__contact_list = self.__contact_list_temp.format(**locals())
        return self.__contact_list
    #A function which adds a new contact to the contacts varaible formatting it with the first_name and last_name which as passed in.
    def create_contact(self, first_name, last_name):
        self.__contacts += self.__contact_temp.format(**locals())

#The individual contact page class which inherits from the page class.
class contactPage(Page):
    #The initilization function.
    def __init__(self):
        #Running the init for the page class.
        Page.__init__(self)
        #The main template for the contact.
        self.__contact_temp = '''
            <section>
                {self.contact_info}
                {self.needs_contact_button}
            </section>'''
        #The contact info tempalte
        self.__contact_info_temp = '''
                <h3>{self.contact.first_name} {self.contact.last_name}</h3>
                <p class="phone_number">{self.contact.phone_number}</p>
                <p class="email">{self.contact.email}</p>
                <p class="company">{self.contact.company}</p>
                <p class="title">{self.contact.title}</p>
                <p class="known_for">Known for {self.contact.known_for} years.</p>'''
        #A variable to hold the contact info template once formatted with the locals.
        self.__contact_info = ''
        #The needs contact button template.
        self.__needs_contact_button_temp = '''
                <p class="needs_contact"><a href="#">It's been a while, send {self.contact.first_name} {self.contact.last_name} a message.</a></p>'''
        #A variable to hold the needs contact button once formatted with the locals.
        self.__needs_contact_button = ''
        #A variable to hold the contact object.
        self.__contact = dict()
        #A variable to hold the contact info template once formatted with the locals.
        self.__contact_html = ''
    #The contact object getter.
    @property
    def contact(self):
        return self.__contact
    #The contact object setter.
    @contact.setter
    def contact(self, contact):
        self.__contact = contact
    #The needs contact button getter.
    @property
    def needs_contact_button(self):
        #Check to see if the needs contact varaible for the contact is true.
        if self.contact.needs_contact:
            #If so create the button from the template formatting it with the locals.
            self.__needs_contact_button = self.__needs_contact_button_temp.format(**locals())
        return self.__needs_contact_button
    #The contact info getter which returns the formatted contact info template.
    @property
    def contact_info(self):
        self.__contact_info = self.__contact_info_temp.format(**locals())
        return self.__contact_info
    #The contact html getter which returns the formatted contact tempalate.
    @property
    def contact_html(self):
        self.__contact_html = self.__contact_temp.format(**locals())
        return self.__contact_html