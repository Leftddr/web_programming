# import webbrowser
import webbrowser


class Movie() :
    """ This class provides a way to store movie related information """

    # class variable (만약 class variable 선언시 constant로 사용할 경우에는 변수이름을 전체 대문자로 함
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # constructor method : instance(object)가 생성될 때 처음에 불려지는 method
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube) :
        # instance varaible 선언 : 반드시 self를 통해 instance variable 선언해야 함
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # instnace method : 함수 argument에 반드시 self가 첫번째 인자로 들어가야 함
    def show_trailer(self) :
        webbrowser.open(self.trailer_youtube_url)
