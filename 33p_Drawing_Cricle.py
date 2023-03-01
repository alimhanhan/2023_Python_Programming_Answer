import turtle

t = turtle.Turtle()
t.shape("turtle")

size = 20
for i in range(80):
    size = size + 2
    t.forward(size)
    t.right(24)