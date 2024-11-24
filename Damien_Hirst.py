# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('download.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle

color_list = [(234, 225, 83), (195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15), (216, 162, 101), (34, 187, 112), (29, 104, 167), (14, 23, 64), (20, 29, 168), (212, 136, 175), (231, 224, 7), (197, 34, 130), (15, 181, 210), (231, 167, 197), (126, 189, 163), (10, 48, 29), (40, 131, 75), (141, 217, 203), (61, 22, 10), (60, 13, 27), (108, 91, 210), (235, 64, 34), (131, 217, 230), (183, 17, 9)]

screen = turtle.Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor("white")

dot_drawer = turtle.Turtle()
dot_drawer.penup()
dot_drawer.hideturtle()
dot_drawer.speed("fastest")

# Draw the 10x10 grid of dots
dot_size = 20  # Each dot is 20 in size
gap = 50  # Spacing between dots


for row in range(10):  # 10 rows
    for col in range(10):  # 10 columns
        dot_drawer.dot(dot_size, color_list[(row * 10 + col) % len(color_list)])
        dot_drawer.forward(gap)  # Move to the next column
    dot_drawer.backward(10 * gap)  # Move back to the start of the row
    dot_drawer.left(90)
    dot_drawer.forward(gap)  # Move up to the next row
    dot_drawer.right(90)

# Exit on click
screen.exitonclick()

