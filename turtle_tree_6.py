#######################################################################################
# This proyect draw a set of 6 recursive multi colour trees
#
# Created by Yeun Jae, Jung in September of 2020 (Barcelona, Spain)
# Contact
#   email: jungyeunjae@gmail.com
#   github: https://github.com/JungPablo
#######################################################################################

import turtle as tur
from colour import get_random_colour


# Recursive function
def draw_tree(i):
    if i<10:
        return
    else:
        tree.color(get_random_colour())
        tree.pensize(i/20)
        tree.forward(i)
        tree.left(30)
        draw_tree(3*i/4)
        tree.right(60)
        draw_tree(3*i/4)
        tree.left(30)
        tree.backward(i)

tree = tur.Turtle()
window = tree.getscreen()
window.bgcolor('black')
tree.pensize(2)
tree.speed(0)
init_x = 0
init_y = -300



tree.goto(init_x, init_y)
tree.left(90)
draw_tree(50) # 1
tree.penup()
init_x -= 200
init_y += 200
tree.goto(init_x, init_y)
tree.pendown()
draw_tree(50) # 2
tree.penup()
init_x += 400
tree.goto(init_x, init_y)
tree.pendown()
draw_tree(50) # 3
tree.penup()
init_x += 200
init_y += 200
tree.goto(init_x, init_y)
tree.pendown()
draw_tree(50) # 4
tree.penup()
init_x -= 400
tree.goto(init_x, init_y)
tree.pendown()
draw_tree(50) # 5
tree.penup()
init_x -= 400
tree.goto(init_x, init_y)
tree.pendown()
draw_tree(50) # 6


tur.done()