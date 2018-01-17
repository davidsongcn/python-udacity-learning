# import 是引入模块（其他.py文件）
# time 模块里面有很多关于 时间的函数 引入以后可以利用里面的函数
import webbrowser
import time
# ctime 就是 time模块里面的一个函数
print("this program starter on" + time.ctime())
# 学会使用while
# 具体用法：定义循环的 初始变量和最终变量
#while 初始变量 < 最终变量 ：
#        执行语句
#初始变量 = 初始变量 + 1
total_break = 3
break_count = 0

while break_count < total_break:
    time.sleep(3)
    webbrowser.open("www.youtube.com")
    break_count = break_count + 1
