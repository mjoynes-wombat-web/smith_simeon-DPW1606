'''
Simeon Smith
7-6-2016
Design Patterns for Web Programming 1606
Simple Form
'''
import webapp2
import logging

class MainHandler(webapp2.RequestHandler):
    def insert_html(self, main, head, title, body, form, user, email):
        head = head.format(**locals())
        body = body.format(**locals())

        return main.format(**locals())

    def get(self):
        main_temp = '''
<!DOCTYPE>
<html>
    {head}
    {body}
</html>
        '''
        head_temp = '''
    <head>
        <title>{title}</title>
    </head>
        '''
        body_temp = '''
    <body>
        {user} {email}
        {form}
    </body>
        '''
        form = '''
        <form method="GET">
            <label>Name: </label><input type="text" name="user" />
            <label>Email: </lable><input type="text" name="email" />
            <input type="submit" value="Submit" />
        </form>
        '''
        title = "Simple Login Form"
        user = ''
        email = ''

        if self.request.GET:
            #store responses
            user = self.request.GET['user']
            email = self.request.GET['email']
            form = ''
            page = self.insert_html(main_temp, head_temp, title, body_temp, form, user, email)
            self.response.write(page)
        else:
            page = self.insert_html(main_temp, head_temp, title, body_temp, form, user, email)
            self.response.write(page)



        
        #self.response.write(page) #Puts info on page.

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
