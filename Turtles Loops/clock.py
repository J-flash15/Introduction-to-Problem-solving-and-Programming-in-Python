#shamarGordon

#duedate 9/14/22

#Turtle loop

import turtle
clock = turtle.Turtle()
clock.shape("turtle")



#for loop draw the turtle clock 

for _ in range(12):
    
    clock.penup()
    
    clock.forward(100)
    
    clock.pendown()
    
    clock.forward(20)
    
    clock.penup()
    
    clock.forward(20)
    
    clock.pendown()
    
    clock.stamp()
    
    clock.penup()
    
    clock.forward(-140)
    
    clock.pendown()
    
    clock.left(30)
