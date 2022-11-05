#shamarGordon
#DueDate: Sep 28, 2022
#Spirals

import turtle


myTurtle = turtle.Turtle()

n = turtle.Screen()
n = turtle.bgcolor("turquoise2")


myTurtle.color("purple")

myTurtle.shape('turtle')

myTurtle.speed(5)

#Spiral

def drawNgon(myTurtle, numSides, sideLength):

            for i in range(numSides):

                myTurtle.pensize(4)

                myTurtle.fd(sideLength)

                myTurtle.left(360/numSides)



numSides = int(input("please enter the number of sides: "))

sideLength = int(input("please enter the size of Length: "))



drawNgon(myTurtle, numSides, sideLength)


