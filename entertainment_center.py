#instancia de filmes

import media
#import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A Marine in an alian planet",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print (avatar.storyline)
#avatar.show_trailer()

movies = [toy_story, avatar]



print (media.Movie.VALID_RATINGS)

print (media.Movie.__module__)
print (media.Movie.__name__)

#fresh_tomatoes.open_movies_page(movies)
