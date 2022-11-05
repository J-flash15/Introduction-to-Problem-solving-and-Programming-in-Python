'''

Alice,Adams,14,13 
Bob,Biggs,18,12
Carl,Carlson,11,14
Donna,Destoyer,9,9
Edna,Enderson,13,20

''''

from datetime import date
import random 


from dataclasses import Field, field
from tkinter import W, Y
from unicodedata import digit


def readFile(raceTime, firstName, lastName ):
    firstName = " "
    lastName  = " "
    raceTime  = []

    for line in raceTime:
         field = line.split(",")
         field = line.split("\n")
         race = open("race.csv", "r")
         firstName.append(field[0])
         lastName.append(str(field[1]))
         raceTime.apppend(int(field[2]))
    race = [ "firstName: ", "lastName: ", "raceTime: " ]
    print(random.choice(race))



# isVowel("q") -> False
# isVowel("e") -> True

def isVowel(c):
    for c in isVowel: 
        c = ["q", "e", ]
    if c  not in isVowel:
        return False
    else: 
        return True

# mostVowels(["Hello", "world", "now"]) -> "Hello"
# mostVowels(["a" , "aei" , "aaaa"]) -> "aaaa"


def mostVowels(words):

    for words in W: 

         words = ["Hello", "world", "now",]

         w = words.count(words)

         print(W)
         mostVowels(words)


#$let
# x = [1,2,3,4,5]
# y = [74,3,4,2,74,75,2]
# z = [2,4,6]
# oddsToZero(x) would x to [0,2,0,4,0]
# oddsToZero(y) would change y to [74,0,4,2,74,0,2]
# oddsToZero(z) would change nothing


def oddsToZero(nums):
    
 y = (int([74,3,4,2,74,75,2]))

for nums in y: 

    nums = complex(y)

    nums = sorted(y)



#japanize("01/13/1999" )-> "1999/01/13"
#japanize("04/06/1958") -> "1958/04/06"


def japanize(date)

    japanize("01/13/1999" )

    date = ("01/13/1999")
    x = sorted(date)

    return date


# digitProduct(351) -> 15
# digitProduct(352) -> 30
# digitProduct(-452) -> 40

def digitProduct(n):

    for n in digit: 

     digit = (351)
    
    n = (351, 352, -452)

    digit = sum(n)


    return digit

     




















    





    
         



    









    





       




     


     




