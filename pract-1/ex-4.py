import turtle

turtle.shape('turtle')
#Нарисуйте 10 вложенных квадратов.
for j in range(10):
    turtle.penup()
    turtle.goto(j*10,j*10)
    turtle.pendown()
    for i in range(4):
       turtle.right(90)
       turtle.forward(50+j*20)
