import media
import fresh_tomatoes

'''
   media의 Movie Class를 가져와 객체를 생성한다.
'''
# Movie class의 instnace(object) 생성
EOTV = media.Movie("Evangelion TV version",
                        "A story of a boy and his toys that comes to life",
                        "https://t1.daumcdn.net/cfile/blog/266EA24058D8B68030",
                        "https://www.youtube.com/watch?v=UP4z85P16cg")
# print (toy_story.storyline)

EOAL = media.Movie("Evangelion: 1.0 You are (Not) Alone",
                     "A marine on an alien planet",
                        "https://draco.pe.kr/wp-content/uploads/2008/02/Evangerion.jpg",
                        "https://www.youtube.com/watch?v=Q3_PS6xa9Uw")
# print (avatar.storyline)
# avatar.show_trailer()
EOA = media.Movie("Evangelion : 2.0 You can (Not) Advance",
                        "Using rock music to learn",
                        "https://i.pinimg.com/originals/cb/a2/35/cba235b5d2d6538b1882612e34b605d7.jpg",
                        "https://www.youtube.com/watch?v=iaY9gGp1l6U")

EOR = media.Movie("Evangelio : 3.0 You can (Not) Redo",
                        "A Rat is a shef in Paris",
                        "https://t1.daumcdn.net/cfile/tistory/025ACB4D51E5ADA824",
                        "https://www.youtube.com/watch?v=4zKZggH-O1I")

EOT = media.Movie("Evangelion : 3.0 + 1.0 Thrice Upon a time ",
                        "Going back in time to meet authors",
                        "https://blog.kakaocdn.net/dn/o3psZ/btqZoydpMUL/9ukjlIi9AwZ1gKyPOme3K1/img.jpg",
                        "https://www.youtube.com/watch?v=gHjr7IY0buw")

EOE = media.Movie("Evangelion : End of Evangelion",
                        "A really real reality show",
                        "https://t1.daumcdn.net/cfile/tistory/99F549425C45C10D08",
                        "https://www.youtube.com/watch?v=GY6LvdsM-3k")

'''
   각 객체를 movies 배열에 넣어 놓는다.
'''
movies = [EOTV, EOAL, EOA, EOR, EOT, EOE]
# open_movies_page 함수 : movies 객체를 input으로 받아 output으로 html file을 생성하고
# html file을 호출하여 web site 보여줌
'''
   이 함수가 어디있는지 알아야 한다.
'''
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
# 아래 __doc__ (""" """을 출력), __name__(class이름 출력), __module__(모듈이름 출력)은 내장된 class 변수임
# ==> (predefined varaibles)
# print (media.Movie.__doc__)
# print (media.Movie.__name__)
# print (media.Movie.__module__)
