#shamarGordon

#duedate 9/14/22

#Turtle loops


import turtle


turtle = turtle.Turtle()

turtle.shape("turtle")

#prompt the user to enter the amount of sides 

n = int(input(" please enter the number of sides you would like to draw: "))


#all the outter angle go by this Equation

l = int(360//n) 


#draw the shape n times 

for _ in range(n):

    turtle.pensize(6)

    turtle.fd(90)

    turtle.lt(l)




  

    

   





