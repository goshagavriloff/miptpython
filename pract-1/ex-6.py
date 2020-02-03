import turtle

turtle.shape('turtle')

#for j in range(10):    эллипс
#    for i in range(180):   эллипс
#       turtle.forward(1)   эллипс
#       turtle.left(1)  эллипс
#    turtle.forward(j*10)   эллипс
#Нарисуйте спираль. См. теорию. Пример:
for js in range(1,25,+1):
    for i in range(9):
        turtle.forward(js)
        turtle.left(20)
