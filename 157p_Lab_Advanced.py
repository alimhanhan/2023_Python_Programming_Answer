import turtle

spi = turtle.Turtle()
size = 16

for i in range(50):
    size = size + 3
    spi.forward(size)
    spi.right(24)