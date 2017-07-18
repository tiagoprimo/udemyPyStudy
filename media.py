import webbrowser

class Movie():
    def __init__(self, movie_title, movie_story_line, movie_poster, movie_trailer_url):
        self.title = movie_title # se tirarmos o self, nenhuma instancia pode acessar este conteudo da variavel, ela vira local.
        self.storyline = movie_story_line
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)