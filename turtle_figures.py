#######################################################################################
# This proyect draw a recursive multi colour polygon
#
# Created by Yeun Jae, Jung in September of 2020 (Barcelona, Spain)
# Contact
#   email: jungyeunjae@gmail.com
#   github: https://github.com/JungPablo
#######################################################################################

import turtle
from colour import get_random_colour


# Draw figure function
def draw_figure(figure, size):
    if size < limit:
        return
    else:
        figure.color(get_random_colour(), get_random_colour())
        figure.begin_fill()
        for i in range(sides):
            figure.forward(size)
            draw_figure(figure, size/divi)
            figure.left(angle)
        figure.end_fill()
        

# Init
figure = turtle.Turtle()
window = figure.getscreen()
window.bgcolor('black')
figure.speed(0)
figure.hideturtle()
figure.shape('circle')
figure.pensize(1)
figure.penup()
figure.goto(-100, -160)
figure.pendown()
size = 150
divi = 3 # when divi grow, nbr of recursion reduce and vice versa
limit = 5 # the smallest element size
sides = 5 # sides number
# angle = 216 # angle for figure drawing
angle = 360/sides # 360 degrees

# Main
draw_figure(figure, size)

turtle.done()