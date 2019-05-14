import turtle
import time

screen = turtle.Screen()

my_turtle = turtle.Turtle()
#my_turtle.hideturtle()
my_turtle.speed(3)
my_turtle.pensize(2)

#screen.delay(0)

start_ticks = time.time()

time_taken = []

lines = []

size = 200

iterations = 4


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def draw_line(line):
    my_turtle.penup()
    my_turtle.setpos(line.a.x, line.a.y)

    my_turtle.pendown()
    my_turtle.setpos(line.b.x, line.b.y)


def calculate_points(line):
    point1 = Position((line.a.x * (2/3) + line.b.x * (1/3)), (line.a.y * (2/3) + line.b.y * (1/3)))
    point2 = Position((line.a.x * (1/3) + line.b.x * (2/3)), (line.a.y * (1/3) + line.b.y * (2/3)))

    return point1, point2


def calculate_top(point1, point2):
    magnitude = ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** (1/2)

    point3 = Position()

    return point3


def subdivide(line):
    point1 = line.a
    point2, point4 = calculate_points(line)
    point3 = calculate_top(point2, point4)
    point5 = line.b

    line1 = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point3, point4)
    line4 = Line(point4, point5)

    return line1, line2, line3, line4


a = Position(-size, -size / 2 * 1.3333333)
b = Position(size, -size / 2 * 1.3333333)
c = Position(0, size / 2 * 1.3333333)

lines.append(Line(a, b))
lines.append(Line(b, c))
lines.append(Line(c, a))

draw_line(lines[0])
draw_line(lines[1])
draw_line(lines[2])

for n in range(iterations):
    #my_turtle.clear()

    new_lines = []

    while len(lines) != 0:
        line1, line2, line3, line4 = subdivide(lines[0])

        new_lines.append(line1)
        new_lines.append(line2)
        new_lines.append(line3)
        new_lines.append(line4)

        lines.remove(lines[0])

    for new_line in new_lines:
        draw_line(new_line)
        lines.append(new_line)

screen.exitonclick()
