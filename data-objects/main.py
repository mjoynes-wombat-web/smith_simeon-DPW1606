import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        luke = Character()
        luke.name = "Luke Skywalker"
        luke.profession = "Jedi Knight"
        luke.age = 26
        luke.home_planet = "Tattooine"

        leia = Character()
        leia.name = "Princess Leia"
        leia.profession = "Princess"
        leia.age = 26
        leia.home_planet = "Alderann"

        yoda = Character()
        yoda.name = "Master Yoda"
        yoda.profession = "Jedi Master"
        yoda.age = 250
        yoda.home_planet = "Degobah"

        chars = [luke, leia, yoda]

        print chars[1].profession

class Character(object):
    def __init__(self):
        self.name = ""
        self.profession = ""
        self.age = 0
        self.home_planet = ""

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
