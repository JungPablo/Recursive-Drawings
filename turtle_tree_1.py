#######################################################################################
# This proyect draw a recursive multi colour tree
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
    if i<15:
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
draw_tree(150) # Calling recursive function



tur.done()