# 第零件事 倒入模块，经常忘记
import os
def rename_file():
# 第一件事，定义函数
    # 第一步，定义路径找到文件和文件名，
    # 并且存为一个变量
    # 路径前面加r 意思是：原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。放置\被转义

    file_list = os.listdir(r"J:\2018.1编程学习\udacity python 印度小哥\第二章，使用函数\photos\prank")
    print(file_list)

    # 切换工作目录
    os.chdir(r"J:\2018.1编程学习\udacity python 印度小哥\第二章，使用函数\photos\prank")

    # 第二部，对每一个文件，重命名
    for file_name in file_list:
        # os.rename(file_name,file_name.lstrip(None,"0123456789"))
        file_name_bytes = str.encode(file_name)
        remove = "123456789"
        table = str.maketrans("", "", remove)
        os.rename(file_name, file_name.translate(table))
    # py3 和py2 有所不同，参照https://stackoverflow.com/questions/43312108/translate-takes-exactly-one-argument-2-given
    # 这个回答帮助了我https: // stackoverflow.com / questions / 39375712 / translate - takes - exactly - one - argument - 2 - given - in -python - error / 43135114  # 43135114?newreg=a4c413e2e5ff470dab888bb611db11e1
    # 2.X版本把字符串基本分为两种：unicode字符串和8位字符串str，后者包含字节数据和我们常见的ASCII码数据；而3.X版本则重新对字符串进行了划分，分为了字节字符串bytes和文本字符串str，两者都是不可变的，所以添加了一个可变的字节字符串类型bytearray。
    # saved_path = os.getcwd()
    # print("this is " + saved_path)
rename_file()

