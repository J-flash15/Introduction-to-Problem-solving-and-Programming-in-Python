#Shamar Gordon

#Oct 17, 2022

#Hurricane Tracker 


import turtle

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)
    
    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")
    
    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """

   
    (t, wn, map_bg_img) = irma_setup()
    
    # your code to animate Irma here

    irma = open("irma.csv", "r")

    text = irma.read()

    line = text.split("\n")[1:]

    mylist = []

    mylist2 = []

    mylist3 = []
   
    
    for row in line:

        
        print(row)
  

        line2 = row.split(",")

        lat = float(line2[2])

        lon = float(line2[3])

        Wind = float(line2[4])

        mylist.append(lat)

        mylist2.append(lon)

        mylist3.append(Wind)


        
        if Wind < 74: 
     
             t.width(0)
             t.pencolor('white')

        elif  Wind < 96:
    
                t.width(4)
                t.pencolor('blue')
                t.write("1",font=('Calibri', 16, 'bold'))


        elif Wind < 111: 
        
            t.width(5)
            t.pencolor('Green')
            t.write("2",font=('Calibri', 16, 'bold'))
                
          
        elif Wind < 130:
       
            t.width(6)
            t.pencolor('Yellow')
            t.write("3", font=('Calibri', 16, 'bold'))

          
        elif Wind < 157:  
                 
            t.width(7)
            t.pencolor('Orange')
            t.write("4", font=('Calibri', 16, 'bold'))

        else:

            t.width(8)
            t.pencolor('Red')
            t.write("5", font=('Calibri', 16, 'bold'))
    
       
       
       
        t.goto(lon,lat)

   
        
    turtle.done()

        

   

if __name__ == "__main__":
    irma()
