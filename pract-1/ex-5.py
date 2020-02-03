import turtle

turtle.shape('turtle')
#Нарисуйте паука с n лапами. Пример n = 12:
n=14
c=360/n

for j in range(n):
    for i in range(2):
        turtle.forward(50)
        turtle.right(180)
        if i==0:
            turtle.stamp()
    turtle.right(c)
