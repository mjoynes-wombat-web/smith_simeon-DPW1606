'''
Simeon Smith
7-6-2016
Design Patterns for Web Programming 1606
Simple Form
'''
import webapp2
import logging

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = '''
<!DOCTYPE>
<html>
    <head>
        <title>Simple Login Form</title>
    </head>
    <body>
        <form method="GET">
            <label>Name: </label><input type="text" name="user" />
            <label>Email: </lable><input type="text" name="email" />
            <input type="submit" value="Submit" />
        </form>
    </body>
</html>
        '''

        if self.request.GET:
            #store responses
            user = self.request.GET['user']
            email = self.request.GET['email']
        
        self.response.write(page) #Puts info on page.

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
