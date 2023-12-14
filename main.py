import turtle as t
from turtle import Turtle, Screen
import random
from turtle import colormode

dany = Turtle()
dany.shape("turtle")
dany.color("DeepPink")
count = 0


#
# direction = [0, 90, 180, 270]
colormode(255)


def col():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


######painting project

#########################creating a spirograpgh
# def draw_spirograph(size_of_gap):
#
#     for _ in range(10000):
#         if _ == 120:
#             print("Now reducing by 1")
#             size_of_gap -=0.5
#         if _ == 300:
#             print("Now reducing by 2")
#             size_of_gap -=0.2
#         if _ == 400:
#             print("Now reducing by 3")
#             size_of_gap -=0.5
#         if _ == 500:
#             print("Now reducing by 3")
#             size_of_gap -=0.7
####################################################3
#         dany.circle(80)
#         dany.setheading(dany.heading() + size_of_gap)
#         dany.speed("fastest")
#         dany.color(col())
# draw_spirograph(5)
#######################################


    # if 50 >= count <= 100:
    #
    #     dany.circle(120)
    #     dany.forward(20)
    #     dany.right(6)
    #     dany.speed("fastest")
    #     dany.color(col())
    #     dany.forward(2)
    #     print(count)
    # elif 100 <= count <= 150:
    #     dany.circle(12)
    #     dany.forward(2)
    #     dany.left(6)
    #     dany.speed("fastest")
    #     dany.color(col())
    #     dany.forward(2)
    #     print(count)
    #
    # else:
        # dany.forward(1)
#
# print(f"total count is {count}")





# for _ in range(200):
#
#     dany.color(col())
#     dany.speed(20)
#     dany.pensize(5)
#     dany.forward(20)
#     dany.setheading(random.choice(direction))



# #this is the code for the turtle drawing many shapes
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         dany.forward(30)
#         dany.speed("fastest")
#         dany.right(angle)
#
# for shape_n in range(2, 60):
#     dany.color(col())
#     draw_shape(shape_n)

# #######################################################################


screen = Screen()
screen.exitonclick()
