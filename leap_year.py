def isLeapYear(year):

    if year % 4 != 0:

        return False
    
     #can now assume divible by 4 

    if  year % 100 == 0:

         if  year % 400 == 0:

             return True

         else:

             return False


         else:

             return True

print(isLeapYear(1999))
print(isLeapYear(1644))
print(isLeapYear(1645))
print(isLeapYear(1000))
print(isLeapYear(1700))


#get inout

date = input("Enter date in MM/DD/YYYY: ")

#assume input is string

#         0123456789
#in form of MM/DD/YYYY

#split date into month, day, year

#variables

month = date[0:2]

day = date [3:5]

year = date [6:]

print(month, day, year)


month = int(month)
day = int(date)
year = int(year)


if month in [4,6,9,11]: #31 day months 

   if  1 <= day <= 30:

       print("valid date")

    else:

        print("invalid day")

elif month in [1,3,5,7,8,10,12]:  #30 day months 

    if  1 <= day <= 31:

       print("valid date")


    elif day == 29


            if isLeapYear()year):

                print("invalid day")

          else:

              print("invalid date is not Leap Year ")

    else:

        print("invalid day")

elif month == 2:  #feb

    
if  1 <= day <= 28:

       print("valid date")

    else:

        print("invalid day")

else:

    print ("Invalid month")
