import turtle
import math

# 좌표축 그리기
line = turtle.Turtle()
line.color("black")

def line1(x1,y1,x2,y2):
    line.up()
    line.goto(x1,y1)
    line.down()
    line.goto(x2,y2)
    return

line1(-500,0,500,0)
line1(0,-500,0,500)

# 코사인 그래프 그리기
t = turtle.Turtle()
t.color("red")

for angle in range(360):
    y = math.cos(math.radians(angle))

    scaledX = angle
    scaledY = y * 100
    t.goto(scaledX, scaledY)