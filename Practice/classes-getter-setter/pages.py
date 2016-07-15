class Page(object):
    def __init__(self):
        self.__title = "Welcome"
        self.__css = "/css/style.css"
        self.html = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" type="text/css" href="{self.css}">
    </head>
    <body id="test">
        {self.body}
    </body>
</html>
        '''
        self.__body = "Welcome to my OOP Python pages!"

        self.whole_page = ""

    def update(self):
        self.whole_page = self.html
        self.whole_page = self.whole_page.format(**locals())

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title
        self.update()

    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, new_css):
        self.__css = new_css
        self.update()

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, new_body):
        self.__body = new_body
        self.update()