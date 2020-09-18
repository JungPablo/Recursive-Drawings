#######################################################################################
# This proyect draw a recursive multi colour star
#
# Created by Yeun Jae, Jung in September of 2020 (Barcelona, Spain)
# Contact
#   email: jungyeunjae@gmail.com
#   github: https://github.com/JungPablo
#######################################################################################

import turtle
from colour import get_random_colour


# Draw star function
def draw_star(size):
    if size < limit:
        return
    else:
        star.color(get_random_colour(), get_random_colour())
        star.begin_fill()
        for i in range(sides):
            star.forward(size)
            draw_star(size/divi)
            star.left(angle)
        star.end_fill()
        

# Init
star = turtle.Turtle()
window = star.getscreen()
window.bgcolor('black')
star.speed(0)
star.hideturtle()
star.shape('circle')
star.pensize(1)
star.penup()
star.goto(-190, 40)
star.pendown()
size = 300
divi = 3 # when divi grow, nbr of recursion reduce and vice versa
limit = 10 # the smallest element size
sides = 5 # sides number
angle = 216 # angle for star drawing
# angle = 360/sides # 360 degrees

# Main
draw_star(size)

turtle.done()