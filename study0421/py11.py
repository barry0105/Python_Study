import turtle

t = turtle.Turtle()
t.shape("turtle")
def square():
    for i in range(4):
        t.forward(50)
        t.left(90)

def drawit(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color("red")
    square()
    t.end_fill

s = turtle.Screen()
s.onscreenclick(drawit)

input()