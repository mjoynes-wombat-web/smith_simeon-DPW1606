class Page(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css/styles.css"
        self.__html = '''
<!DOCTYPE HTML>
<html>
    {head}
    {body}
</html>
        '''
        self.__head = '''
    <head>
        <title>Enter your information:</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css">
    </head>
        '''

        self.body = '''
    <body>
        {content}
    </body>
        '''
        self.__error = ""

    def print_out(self, content, span):
        page_html = self.__html
        head = self.__head
        body = self.body
        body = body.format(**locals())
        page_html = page_html.format(**locals())

        return page_html