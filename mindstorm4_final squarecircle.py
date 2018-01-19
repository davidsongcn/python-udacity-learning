import turtle
# brad_turtle 在括号里，预先定义函数的参数（不用声明，直接赋予一个变量），在函数中可以直接，在这个变量上添加方法
def draw_square(brad_turtle):
    # range以后一个参数结束但不包括end
    for i in range(1,5):
        brad_turtle.forward(100)
        brad_turtle.right(90)
        brad_turtle.speed(9)
def draw_picture():
    window = turtle.Screen()
    window.bgcolor("orange")
    # 实例化一个类
    # 类有很多方法，直接实例.方法.(参数)
    brad = turtle.Turtle()
    brad.color("blue")
    brad.shape("circle")
    brad.speed(7)

    # 改进循环

    for i in range(1,31):
        # 如果定义的时候就有参数，函数一定要带参数，参数就是变量，就是类的实例，这个参数下面有很多方法
        draw_square(brad)
        brad.right(30)

    # 旋转循环
    # count_final = 24
    # count_count = 0
    # p = 0 #让每次加速
    # while count_count < count_final:
    #
    #     draw_square(brad)
    #     count_count = count_count + 1
    #     p = p + 19 #让每次加速
    #     brad.right(20 + p)



    # 再画一个圆圈
    # angie = turtle.Turtle()
    # angie.circle(100)
    #
    # # 再画一个三角形
    # # triangle1 = turtle.Turtle()
    # # count_stop1 = 3
    # # count_count1 = 0
    # # while count_count1 < count_stop1:
    # #     triangle1.forward(100)
    # #     triangle1.right(120)
    # #     count_count1 = count_count1 + 1

    window.exitonclick()
draw_picture()
