#Lab2: Messy Chocolate
#Student name: Shamar J Gordon
#DUE Sep 7


seconds = int(input("Enter a total number of seconds: "))

hours = seconds // 3600

seconds %= 3600

minutes = seconds // 60

seconds %= 60

hour = minutes * 60


print( hours, "hours", minutes, "minutes", seconds, "seconds" )




