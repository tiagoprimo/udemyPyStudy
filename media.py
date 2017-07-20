# coding=utf-8
import webbrowser


class Video():
    # definição de uma constante, sempre maiusculas
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, duration):
        print ("Estou na classe video")
        self.title = title
        self.duration = duration

    def show_title(self):
        print (self.title)

    def show_duration(self):
        print (self.duration)


class Movie(Video):
    """ fazer um comentário no estilo deste abaixo, preenche a variavel __doc__ do python, permitindo imprimier as informações da classe
    com a chamada print(media.Movie.__doc__)
    This class provides a way to store movie related information"""
    print ("Estou na classe video")

    def __init__(self, movie_title, movie_duration, movie_story_line, movie_poster, movie_trailer_url):
        # se tirarmos o self, nenhuma instancia pode acessar este conteudo da variavel, ela vira local.
        Video.__init__(self, movie_title, movie_duration)
        self.storyline = movie_story_line
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    def __init__(self, series_title, series_duration, season, episode, tv_station):
        Video.__init__(self, series_title, series_duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def show_season(self):
        print (self.season)

    def show_episode(self):
        print (self.episode)

    def show_tv_station(self):
        print (self.tv_station)



seinfield = TvShow("Seinfield", "30 Min", "3", "21", "Warner")

seinfield.show_title()
seinfield.show_duration()
seinfield.show_season()
seinfield.show_episode()
seinfield.show_tv_station()