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



def drawRow(myTurtle, length, squareSize):


    for i in range(length):

        drawSquare(myTurtle, squareSize)

        myTurtle.forward(squareSize)
            
        
row = int(input("Enter the number square: "))

num = int(input("Enter the size of square: "))
drawRow(myTurtle, row, num)
