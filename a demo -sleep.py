import webbrowser
import time
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
