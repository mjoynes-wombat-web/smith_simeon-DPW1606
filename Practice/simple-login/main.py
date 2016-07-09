'''
Simeon Smith
7-6-2016
Design Patterns for Web Programming 1606
Simple Form - Practice
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def insert_html(self, main, head, title, body, form, user, email, links):
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
        {links}
    </body>
        '''

        form = '''
        <form method="GET">
            <label>Name: </label><input type="text" name="user" />
            <label>Email: </lable><input type="text" name="email" />
            <input type="submit" value="Submit" />
        </form>
        '''

        links = '''
        <p>
            <a href="?email=bob@bill.com&user=bob">Click here if your email is bob@bill.com</a><br/>
            <a href="?email=james@bill.com&user=james">Click here if your email is james@bill.com</a><br/>
            <a href="?email=richard@bill.com&user=richard">Click here if your email is richard@bill.com</a><br/>
            <a href="?email=henry@bill.com&user=henry">Click here if your email is henry@bill.com</a><br/>
        </p>
        '''

        title = "Simple Login Form"
        user = ''
        email = ''

        if self.request.GET:
            #store responses
            user = self.request.GET['user']
            email = self.request.GET['email']
            form = ''
            links = ''
            page = self.insert_html(main_temp, head_temp, title, body_temp, form, user, email, links)
            self.response.write(page)
        else:
            page = self.insert_html(main_temp, head_temp, title, body_temp, form, user, email, links)
            self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
