#######################################################################################
# This proyect draw a multi colour snow
#
# Created by Yeun Jae, Jung in September of 2020 (Barcelona, Spain)
# Contact
#   email: jungyeunjae@gmail.com
#   github: https://github.com/JungPablo
#######################################################################################


from turtle import *
from colour import get_random_colour


bgcolor('black')
goto(-200, 0)
speed(0)


# begin_fill()
for i in range(72):
    color(get_random_colour())
    forward(400)
    left(175)
    if abs(pos()) < 1:
        break
# end_fill()
done()