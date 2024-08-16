import turtle as t
def cubemaker():
    go1=t.Turtle()
    go2=t.Turtle()
    go1.hideturtle()
    go2.hideturtle()
    bg=t.Screen()
    bg.bgcolor("black")
    go1.pencolor("Red")
    go2.pencolor("Yellow")
    for i in range (0,4):
        go1.fd(150)
        go1.lt(90)
    go2.lt(90)
    go2.penup()
    go2.fd(35)
    go2.pendown()
    go2.lt(90)
    go2.fd(75)
    for i in range(0,3):
        go2.rt(90)
        go2.fd(150)
    go1.lt(90)
    for i in range(0,4):
        if i%2==0:
            go1.pencolor("Red")
        else:
            go1.pencolor("Yellow")
        go2.rt(90)
        go2.fd(150)
        x,y=go2.pos()
        z,n=go1.pos()
        go1.pendown()
        go1.goto(x,y)
        go1.penup()
        go1.goto(z,n)
        go1.fd(150)
        go1.rt(90)
