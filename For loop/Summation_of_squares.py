#shamargordon
#Duedate sep 28, 2022
#Summation_of_squares

def manySummation (n):

        total = 0

        for i in range(n + 1):

            total += (i**2)

        print(total)  
      
n = int(input("please enter a number: "))
manySummation(n)        
