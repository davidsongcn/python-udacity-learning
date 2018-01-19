from urllib.request import urlopen
#第一步先定义函数，使用函数
def read_text():
    # 实例化----使用open函数（函数是不依托于类的，方法是在类中的函数，并且open太常用是built-in函数，意思是自带函数） 创建一个file对象quotes，之后的操作可以利用file类下的各种方法，
    # 字符串中的r 排除转意符
    quotes = open(r"J:\2018.1编程学习\udacity python 印度小哥\第二章，使用函数\movie_quotes.txt")
    # 任何抽象的储存空间都要有一个 变量来储存，
    # 我第一次操作的时候没有给 quotes.read（）赋予变量
    contents_of_file = quotes.read()
    print(contents_of_file)

    # 养成好习惯，最后关闭文件
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    # urlopen 类似于 open 用于打开url
    connection = urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()


read_text()
