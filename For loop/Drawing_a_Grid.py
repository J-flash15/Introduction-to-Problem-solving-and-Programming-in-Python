#shamarGordon
#DueDate: Sep 28, 2022
#Teenage Mutant Function Turtles


import turtle

myTurtle = turtle.Turtle()
wn = turtle.Screen()
wn = turtle.bgcolor("LightSkyBlue1")
myTurtle.color("purple")
myTurtle.shape('turtle')
myTurtle.speed(2)

def drawSquare(myTurtle, squareSize):

 
    for i in range(4):
            myTurtle.forward(squareSize)
            myTurtle.rt(90)



def drawRow(myTurtle, length, squareSize):


    for i in range(length):

        drawSquare(myTurtle, squareSize)

        myTurtle.forward(squareSize)



def drawGrid(myTurtle, size, squareSize):

    for i in range(size):

        drawRow(myTurtle, size, squareSize)

        myTurtle.backward(squareSize * size)


        myTurtle.right(90)


        myTurtle.forward(squareSize)


        myTurtle.left(90)

               
        
row = int(input("Enter the number square: "))

num = int(input("Enter the size of square: "))


drawGrid(myTurtle, row, num)








