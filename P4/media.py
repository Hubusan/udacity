""" This is the movie class definition to hold information about movies"""
import webbrowser

class Movie():
    """
        This part defines the variables that all instances of this class will have.
        movie_title --> Will keep Movie Title
        movie_storyline --> Will keep storyline of the movie
        poster_image --> this will keep the url for the poster image of the movie
        trailer_youtube --> this will keep the url for the trailer
        
    """
    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
        self.title = movie_title                                                                #variable to hold movie title
        self.stroyline = movie_storyline                                                        #variable to hold stroyline
        self.poster_image_url = poster_image_url                                                #variable to hold image url
        self.trailer_youtube_url = trailer_youtube_url                                          #variable to hold video url
    
