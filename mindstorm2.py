import turtle


def draw_picture():
    window = turtle.Screen()
    window.bgcolor("orange")

    brad = turtle.Turtle()
    brad.color("blue")
    brad.shape("circle")
    brad.speed(3)

    # 改进循环
    count_stop = 4
    count_count = 0
    while count_count < count_stop:
        brad.forward(100)
        brad.right(90)
        count_count = count_count + 1

    # 再画一个圆圈
    angie = turtle.Turtle()
    angie.circle(100)

    # 再画一个三角形
    triangle1 = turtle.Turtle()
    count_stop1 = 3
    count_count1 = 0
    while count_count1 < count_stop1:
        triangle1.forward(100)
        triangle1.right(120)
        count_count1 = count_count1 + 1

    window.exitonclick()
draw_picture()
