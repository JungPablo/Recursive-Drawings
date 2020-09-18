#######################################################################################
# Random colour module
# This Module choice a random colour and return that
#
# Created by Yeun Jae, Jung in September of 2020 (Barcelona, Spain)
# Contact
#   email: jungyeunjae@gmail.com
#   github: https://github.com/JungPablo
#######################################################################################


from random import choice


# Random color function
def get_random_colour():
    colour_list = [
                '0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'
                ]
    colour_code = '#'
    for i in range(6):
        colour_code += choice(colour_list)
    return colour_code
