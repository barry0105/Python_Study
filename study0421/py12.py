import turtle
t = turtle.Turtle()
t.shape("turtle")
def maze(x, y):
    for i in range(2):
        t.penup()
        if i == 1:
            t.goto(x+100, y+100)
        else:
            t.goto(x,y)
        t.pendown()
        t.forward(200)
        t.right(90)
        t.forward(90)
        t.left(90)
        t.forward(200)
        t.penup()
    t.goto(x,(y+(y+100))/2)
def turn_left():
    t.left(10)
def turn_right():
    t.right(10)
s = turtle.Screen()
maze(-200, 150)
t.speed(1)
t.pendown()
s.onkey(turn_left, "Left")
s.onkey(turn_right,"Right")
s.listen()
s.mainloop()