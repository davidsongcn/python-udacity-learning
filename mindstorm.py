import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor("orange")

    brad = turtle.Turtle()
    brad.color("blue")
    brad.shape("circle")
    brad.speed(1)

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    # 再画一个圆圈
    angie = turtle.Turtle()
    angie.circle(100)

    window.exitonclick()




draw_square()