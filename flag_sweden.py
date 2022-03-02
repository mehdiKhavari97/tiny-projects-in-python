import turtle
from turtle import *

turtle.colormode(255)
wn=turtle.Screen()
wn.bgcolor(0, 106, 167)
wn.title("I LOVE SWEDEN")

speed(3)
setup(800, 500)

penup()
goto(-400, -50)
pendown()

# Blue Cross
color(254, 204, 2)
begin_fill()
forward(800)
left(90)
forward(100)
left(90)
forward(800)
end_fill()

penup()
goto(-100, -250)
pendown()

begin_fill()
forward(100)
right(90)
forward(500)
right(90)
forward(100)
end_fill()

hideturtle()

turtle.done()
