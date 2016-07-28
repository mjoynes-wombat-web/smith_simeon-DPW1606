class Page(object):
    def __init__(self):
        self.__html_temp = '''
<!DOCTYPE html>
<html lang="en">
{self.head}
{self.body}
</html>'''
        self.__head_temp = '''
<head>
    <title>{self.title}</title>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css?family=Arima+Madurai:800|Lato:300,400" rel="stylesheet">
    <link href="css/{self.css}" rel="stylesheet">
</head>'''
        self.__body_temp = '''
<body>
    {self.header}
    {self.main}
</body>
        '''
        self.__header_temp = '''
        <header>
            <h1>{self.h1}</h1>
        </header>'''
        self.__header = ''
        self.__main = ''
        self.__title = ''
        self.__css = ''
        self.__head = ''
        self.__html = ''
        self.__body = ''
        self.__h1 = ''

    @property
    def html(self):
        self.__html = self.__html_temp.format(**locals())
        return self.__html

    @property
    def head(self):
        self.__head = self.__head_temp.format(**locals())
        return self.__head

    @property
    def body(self):
        self.__body = self.__body_temp.format(**locals())
        return self.__body

    @property
    def header(self):
        self.__header = self.__header_temp.format(**locals())
        return self.__header

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, css):
        self.__css = css

    @property
    def main(self):
        return self.__main

    @main.setter
    def main(self, main):
        self.__main = main

    @property
    def h1(self):
        return self.__h1

    @h1.setter
    def h1(self, h1):
        self.__h1 = h1

class contactPage(Page):
    def __init__(self):
        Page.__init__(self)
