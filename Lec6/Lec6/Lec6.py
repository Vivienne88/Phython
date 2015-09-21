class Movie :
    '''영화 클래스 입니다.'''
    count = 0
    title = "혹성탈출"
    director = "원숭원숭"
    def __init__(self, title, director) :
        self.title = title
        self.director = director
        Movie.count+=1
        print(self.title + " 생성자 호출")

    def showInfo(self) :
        print(self.title + " " + self.director + "\n")

    def __del__(self) :
        print(self.title + " 소멸자 호출")

    @staticmethod
    def showCount() :
        print(Movie.count)

    @classmethod
    def showCount2(cls) :
        print(cls.count)

m1 = Movie("1","A")
m2 = Movie("2","B")
m3 = Movie("3","C")
m4 = Movie("4","D")
m5 = Movie("5","E")
m6 = Movie("6","F")

Movie.showCount()
Movie.showCount2()


