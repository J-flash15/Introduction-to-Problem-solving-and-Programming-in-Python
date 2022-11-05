#Shamar Gordon

#October 9 2022

#Cash


def isfloat(myinput):

   numDec = myinput.count(".")

   if numDec > 1:

      return False

   num =  myinput.split(".")

   for i in num:

      if i.isdigit() == False:

         return False

   return True
  
   
while True:
    
    userinput = input("Please Enter the Change owed: ")

    if isfloat(userinput): 
    
       change = int(float(userinput)*100)

       coins = 0
       
       if change > 0 :
           
           
           quarters = int(change / 25)


           dimes = int((change % 25) / 10 )


           nickels = int(((change % 25) % 10) / 5)


           pennies = int(((change % 25) % 10) % 5)


           coins = coins + quarters


           coins = coins + dimes


           coins = coins + nickels
      

           coins = coins + pennies


           print(coins)
        
    

    






     

     

    


    

    
      
    

      
     

        
     
    


    
