"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media
"""
    Definition of the main function to start movie web page generation
"""
def main():
        matrix = media.Movie("The Matrix",                                                                  #Generating an instance of media to keep the data of the movie matrix                                                                                             
                             "The world is a simulation",
                             "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                             "https://www.youtube.com/watch?v=Q8g9zL-JL8E")
        
        lordoftherings = media.Movie("The Lord of The Rings",
                                     "One ring to rule them all.",
                                     "https://imgc.allpostersimages.com/img/posters/lord-of-the-rings-fellowship-of-the-ring_u-L-F5602Z0.jpg?src=gp&w=300&h=375",
                                     "https://www.youtube.com/watch?v=Pki6jbSbXIY")

        movies = [matrix,lordoftherings]                                                                    #putting all the movies into a list to be used in other method call
        fresh_tomatoes.open_movies_page(movies)                                                             #calling fresh_tomatoes open_movies_page to generate new html with our data given above

main()
                                     
                                     
