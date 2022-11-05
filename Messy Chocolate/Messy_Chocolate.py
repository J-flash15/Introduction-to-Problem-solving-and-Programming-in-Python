#Lab2: Messy Chocolate
#Student name: Shamar J Gordon
#DUE Sep 7 


weight = int(input(" Enter Weight in pounds: \n"))

               
height = int(input(" Enter Height in inches: \n"))
               
age = int(input(" Enter age in years: \n"))

w = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

m = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)



print("number of chocolate bars that should be consumed: \n")

print("mmen should consume: ", m // 214)

print("women should consume: ", w // 214)
