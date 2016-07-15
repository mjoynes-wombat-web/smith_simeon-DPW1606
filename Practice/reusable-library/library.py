class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []

    def add_movie(self, m):
        self.__movie_list.append(m)
        #print m.title

    def compile_list(self):
        output = ''
        for movie in self.__movie_list:
            output += 'Title: ' + movie.title + ' (' + str(movie.year) + ') Directed by: ' + movie.director + '<br>'
        output += '{span}'

        return output

    def calc_time_span(self):
        years = []
        
        for movie in self.__movie_list:
            years.append(movie.year)

        years.sort()

        span = years[len(years)-1] - years[0]

        return 'The span between films entere is ' + str(span) + '.'
        
class MovieData(object):
    def __init__(self):
        self.title = ''
        self.__year = 0 #check for valid year
        self.director = ''
        
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if y > 2016:
            print "Error, invalid date!"
            self.__year = 2014
        else:
            self.__year = y