import turtle
import time
from matplotlib import pyplot as plt

screen = turtle.Screen()

my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.speed(0)
my_turtle.pensize(2)

screen.delay(0)

start_ticks = time.time()

time_taken = []

triangles = []

size = 200

iterations = 5


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


def draw_line(start, end):
    my_turtle.penup()
    my_turtle.setpos(start.x, start.y)

    my_turtle.pendown()
    my_turtle.setpos(end.x, end.y)


def draw_triangle(triangle):
    draw_line(triangle.a, triangle.b)
    draw_line(triangle.b, triangle.c)
    draw_line(triangle.c, triangle.a)


def subdivide(triangle):
    ab = Position((triangle.a.x + triangle.b.x) / 2, (triangle.a.y + triangle.b.y) / 2)
    bc = Position((triangle.b.x + triangle.c.x) / 2, (triangle.b.y + triangle.c.y) / 2)
    ac = Position((triangle.a.x + triangle.c.x) / 2, (triangle.a.y + triangle.c.y) / 2)

    triangle1 = Triangle(triangle.a, ab, ac)
    triangle2 = Triangle(ab, triangle.b, bc)
    triangle3 = Triangle(ac, bc, triangle.c)

    return triangle1, triangle2, triangle3


a = Position(-size, -size / 2 * 1.3333333)
b = Position(size, -size / 2 * 1.3333333)
c = Position(0, size / 2 * 1.3333333)

main_triangle = Triangle(a, b, c)

triangles.append(main_triangle)

draw_triangle(main_triangle)

for n in range(iterations):
    new_triangles = []

    time_taken.append(time.time() - start_ticks)

    while len(triangles) != 0:
        new_triangle1, new_triangle2, new_triangle3 = subdivide(triangles[0])

        new_triangles.append(new_triangle1)
        new_triangles.append(new_triangle2)
        new_triangles.append(new_triangle3)

        triangles.remove(triangles[0])

    for triangle in new_triangles:
        draw_triangle(triangle)

        triangles.append(triangle)

screen.exitonclick()

plt.plot(time_taken)

#plt.show()
