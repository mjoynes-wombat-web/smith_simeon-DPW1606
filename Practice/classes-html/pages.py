class Page(object):
    def __init__(self):
        self.title = "Welcome"
        self.css = "/css/style.css"
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
        self.body = "Welcome to my OOP Python pages!"

    def print_out(self):
        html = self.html
        html = html.format(**locals())
        return html