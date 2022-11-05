#Shamar Gordon

#October 9, 2022

#mario Pyramind 


height = 0



while height > 8 or height < 1:


  
    height = int(input("Please Enter the Height: "))


for i in range(1, height + 1):
    

    for k in range(1, height + 1):

    


         if k > (height - i):


                print("#", end="")

         else:

                print ( " ", end="")


         if  k == height:

            print(" ", "#" * i, end="")

    print()
