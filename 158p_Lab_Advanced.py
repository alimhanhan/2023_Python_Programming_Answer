import turtle

octagon = turtle.Turtle()

sides = 8
side_length = 133
angle = 360.0 / sides

for i in range(sides):
    octagon.forward(side_length)
    octagon.right(angle)