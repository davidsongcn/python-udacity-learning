import webbrowser

# 根据google的代码风格指南，类的首字母最好大写
class Movie():
    """测试一下doc行不行"""
    # 类变量,所有实例都共享的变量，实例变量只针对某个实例自身，变量前面必须加实例名字，类变量定义在类的定义之后，实例变量则是以为self.开头
    # 对常量变量 最好全用大写
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # 不管是init还是自定义的show——traler方法，都采用第一个变量 self
    def show_trailer(self):
        # 下面的参数利用了上面的实力参数self.trailer_youtube_url
        webbrowser.open(self.trailer_youtube_url)

