#shamarGordon
#DueDate: Sep 28, 2022
#Super Spiral

import turtle


myTurtle = turtle.Turtle()

n = turtle.Screen()
n = turtle.bgcolor("turquoise2")


myTurtle.color("purple")

myTurtle.shape('turtle')

myTurtle.speed(0)



def drawNgon(myTurtle, numSides, sideLength):

            for i in range(numSides):

                myTurtle.pensize(4)

                myTurtle.fd(sideLength)

                myTurtle.left(360/numSides)

               


def drawNgonSpiral(myTurtle, numSides, sideLength, numShapes):

            for i in range(numShapes):

                drawNgon(myTurtle, numSides, sideLength)

                myTurtle.right(720/numShapes)

               

                

numSides = int(input("please enter the number of sides: "))

sideLength = int(input("please enter the sides of Length: "))

numShapes = int(input("please enter the number of shapes: " ))

drawNgonSpiral(myTurtle, numSides, sideLength, numShapes)

