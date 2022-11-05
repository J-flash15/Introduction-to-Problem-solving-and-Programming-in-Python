#shamarGordon
#DueDate: Sep 28, 2022
#Teenage Mutant Function Turtles


import turtle


myTurtle = turtle.Turtle()

myTurtle.color("purple")

myTurtle.shape('turtle')

myTurtle.speed(4)

def drawSquare(myTurtle, squareSize):

 
    for i in range(4):
            myTurtle.forward(squareSize)
            myTurtle.rt(90)
        
n = int(input("Enter the length of the size of the square: "))
drawSquare(myTurtle, n)
