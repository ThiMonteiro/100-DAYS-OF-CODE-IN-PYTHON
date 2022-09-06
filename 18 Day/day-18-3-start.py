import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########
colours = ["blue", "lime", "firebrick", "dark red"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
