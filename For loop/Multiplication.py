#Shamar Gordon
#due date Sep 28, 2022
#Multiplication Table



def manyMultiplication (n):
 
  
        for i in range(n):
                
                for x in range(n):

                        print((x + 1) * (i + 1), "  ", end="")

                print()


                

n = int(input("Enter the number of multiplication table: "))
manyMultiplication(n)
 
