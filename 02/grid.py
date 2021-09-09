import turtle

xCnt = 0
yCnt = 0

turtle.right(90)
while(xCnt < 6):
    turtle.penup()
    turtle.goto(xCnt * 100 - 200, 300)
    turtle.pendown()
    turtle.forward(500)
    xCnt += 1

turtle.right(90)
while(yCnt < 6):
    turtle.penup()
    turtle.goto(300, yCnt * 100 - 200)
    turtle.pendown()
    turtle.forward(500)
    yCnt += 1

turtle.exitonclick()
