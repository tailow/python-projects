import turtle
import math

size = 200

my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.speed(0)

screen = turtle.Screen()
screen.delay(0)

points = []
lines = []

a = 0.5
b = 2
iterations = 8
gap = 0.5
width = 380
scale = 100


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def f(x, n):
    return pow(a, n) * math.cos(pow(b, n) * math.pi * x)


def draw_line(line):
    my_turtle.penup()
    my_turtle.setpos(line.a.x, line.a.y)

    my_turtle.pendown()
    my_turtle.setpos(line.b.x, line.b.y)


i = -width / scale

while i <= width / scale:
    y = 0

    for n in range(iterations):
        y += f(i, n)

    point = Vector2(i * scale, y * scale)
    points.append(point)

    i += gap / scale

for i in range(len(points) - 1):
    line = Line(points[i], points[i + 1])
    lines.append(line)

for line in lines:
    draw_line(line)

screen.exitonclick()
