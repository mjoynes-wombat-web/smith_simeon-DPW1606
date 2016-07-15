
import webapp2
from pages import Page
from library import MovieData, FavoriteMovies

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()
        lib = FavoriteMovies()

        #USER ENTRY
        #Movie Title
        #Year Made
        #Directory
        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.director = "Rob Reiner"
        md1.year = 1989
        lib.add_movie(md1)

        md2 = MovieData()
        md2.title = "Dune"
        md2.director = "David Lynch"
        md2.year = 1986
        lib.add_movie(md2)

        md3 = MovieData()
        md3.title = "Star Wars"
        md3.director = "George Lucas"
        md3.year = 1977
        lib.add_movie(md3)

        p.body = lib.compile_list()

        self.response.write(p.print_out(p.body, lib.calc_time_span()))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
