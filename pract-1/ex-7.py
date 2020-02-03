import turtle

turtle.shape('turtle')
#Нарисуйте «квадратную» спираль. 
for js in range(0,145,+5):
    for i in range(2):
        turtle.forward(js)
        turtle.left(90)
