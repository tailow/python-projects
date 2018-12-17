import turtle

screen = turtle.Screen()

screen.bgcolor("yellow")

pietari = turtle.Turtle()
pietari.speed(20)

pietari.penup()
pietari.goto(-50, -200)
pietari.pendown()

pietari.begin_fill()
pietari.circle(50, 360)
pietari.end_fill()

pietari.penup()
pietari.goto(50, -200)
pietari.pendown()

pietari.begin_fill()
pietari.circle(50, 540)
pietari.end_fill()

pietari.begin_fill()
pietari.goto(50, 250)

pietari.setheading(90)
pietari.circle(50, 180)

pietari.goto(-50, -150)
pietari.goto(50, -150)
pietari.end_fill()

screen.exitonclick()