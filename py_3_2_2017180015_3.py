import turtle

count1 = 0
turtle.penup()
turtle.goto(- 250,250)
turtle.pendown()
while count1<5:
    if count1 % 2 == 0:
       turtle.forward(500)
       turtle.right(90)
       turtle.forward(100)
       turtle.right(90)
       count1 = count1 + 1
    elif count1 % 2 == 1 or count1 % 2 == 2:
        turtle.forward(500)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        count1 = count1 + 1


turtle.forward(500)

turtle.right(90)

count2 = 0
while count2<5:
    if count2 % 2 == 0:
       turtle.forward(500)
       turtle.right(90)
       turtle.forward(100)
       turtle.right(90)
       count2 = count2 + 1
    elif count2 % 2 == 1 or count2 % 2 == 2:
        turtle.forward(500)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        count2 = count2 + 1


turtle.forward(500)
