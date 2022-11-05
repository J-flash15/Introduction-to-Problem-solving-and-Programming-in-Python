#shamarGordon
#DueDate: Sep 28, 2022
#Drawing a Stair of Squares
import turtle


myTurtle = turtle.Turtle()

wn = turtle.Screen()
wn = turtle.bgcolor("turquoise2")


myTurtle.color("purple")

myTurtle.shape('turtle')

myTurtle.speed(5)

def drawSquare(myTurtle, squareSize):

 
    for i in range(4):
            myTurtle.forward(squareSize)
            myTurtle.rt(90)


def drawRow(myTurtle, length, squareSize):


    for i in range(length):

        drawSquare(myTurtle, squareSize)

        myTurtle.forward(squareSize)


        
def drawSquareStairs(myTurtle, height, squareSize):

 

    for i in range(height):

        myTurtle.goto(0,squareSize * ( i ))

        drawRow(myTurtle, height - i , squareSize)

        myTurtle.backward(squareSize * (height - i))

        myTurtle.left(90)

        myTurtle.right(90)
       

        
        
       
        
            
row = int(input("Enter the number square: "))

num = int(input("Enter the size of the square: "))

drawSquareStairs(myTurtle, row, num)


