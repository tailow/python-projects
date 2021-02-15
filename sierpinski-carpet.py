import math
import turtle

size = 200

my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.speed(0)

screen = turtle.Screen()
screen.delay(0)

squares = []

iterations = 4


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Square:
    def __init__(self, a, b, c, d, color, center):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.center = center

        self.color = color


def draw_line(a, b):
    my_turtle.penup()
    my_turtle.setpos(a.x, a.y)

    my_turtle.pendown()
    my_turtle.setpos(b.x, b.y)


def draw_square(square):
    my_turtle.fillcolor(square.color)

    my_turtle.begin_fill()

    draw_line(square.a, square.b)
    draw_line(square.b, square.c)
    draw_line(square.c, square.d)
    draw_line(square.d, square.a)

    my_turtle.end_fill()


def define_square(center, side_length, color):
    a = Vector2(center.x - side_length / 2, center.y - side_length / 2)
    b = Vector2(center.x + side_length / 2, center.y - side_length / 2)
    c = Vector2(center.x + side_length / 2, center.y + side_length / 2)
    d = Vector2(center.x - side_length / 2, center.y + side_length / 2)

    return Square(a, b, c, d, color, center)


def subdivide(square):
    side_length = square.b.x - square.a.x

    subdivided_squares = []

    y = square.a.y + side_length / 6

    while y < square.d.y:
        x = square.a.x + side_length / 6

        while x < square.b.x:
            if len(subdivided_squares) == 4:
                subdivided_squares.append(define_square(Vector2(x, y), side_length / 3, "white"))
                draw_square(define_square(Vector2(x, y), side_length / 3, "white"))

            else:
                subdivided_squares.append(define_square(Vector2(x, y), side_length / 3, "black"))

            x += side_length / 3
        y += side_length / 3

    return subdivided_squares


a = Vector2(-size, -size)
b = Vector2(size, -size)
c = Vector2(size, size)
d = Vector2(-size, size)

main_square = Square(a, b, c, d, "black", Vector2(0, 0))

squares.append(main_square)

draw_square(main_square)

for n in range(iterations):
    new_squares = []

    while len(squares) != 0:
        for square in subdivide(squares[0]):
            new_squares.append(square)

        squares.remove(squares[0])

    for new_square in new_squares:
        if new_square.color != "white":
            squares.append(new_square)

screen.exitonclick()
