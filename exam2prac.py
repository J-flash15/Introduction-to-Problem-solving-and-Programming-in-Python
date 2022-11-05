
"""
11/11/19,64,40
11/12/19,49,21
11/13/19,33,22
"""
from csv import field_size_limit
from dataclasses import field


def readFile(filename):
    dates = [] 
    highs = []
    lows = []
    data = open(filename, "r")
    for line in data:
        fields = line.split(",")
        dates.append(fields[0])
        highs.append( int(fields[1]))
        lows.append( int(fields[2]))

    return dates, highs, lows


def highestHigh(dates, highs):
    highestDay =  ""#dates[0]
    highestTemp = -124889 #highs[0]
    #for index in range(len(dates)):
    for index, date in enumerate(dates):
        dailyTemp = highs[index]
        if dailyTemp > highestTemp :
            highestTemp = dailyTemp
            highestDay = date
    return highestDay


def lowestLow(dates, lows):
    lowestDay =  ""#dates[0]
    lowestTemp = 124889 #low[0]
    #for index in range(len(dates)):
    for index, date in enumerate(dates):
        dailyTemp = lows[index]
        if dailyTemp < lowestTemp :
            lowestTemp = dailyTemp
            lowestDay = date
    return lowestDay

def avgHighs(highs):
    numHighs = 0
    sumHighs = 0
    for temp in highs:
        numHighs += 1 
        sumHighs += temp
    return sumHighs/numHighs
    
    #return sum(highs)/len(highs)


def readFileAndSum(filename):
    data =  open(filename, "r")
    total = 0
    for line in data:
        fields =  line.split(",")
        for n in fields:
            n = int(n)
            if n % 2== 0:
                total += n

    return total


# unOrUn("untied") -> "tied"
# unOrUn("unable") -> "able"
# unOrUn("necessary") -> "unnecessary"
def unOrUn(word):
    if word[0:2] =="un":
    #if word[0] == "u" and word[1] == "n":
        return word[2:]
    else:
        return "un" + word


# [1,2,3,4,5] -> 4
# [15,31,21,17,28] -> 16
# [-1,-100,12,2,100] -> 200
def maxMinDiff(numbers):
    biggest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num > biggest:
            biggest = num
        if num < smallest:
            smallest = num



    return biggest -smallest
    #return max(numbers) - min(numbers)

# [1,2,3,4,5] -> [5,2,3,4,1]
#  [15,31,21,17,28] -> [28,31,21,17,15]
# [-1,-100,12,2,100] -> [100,-100,12,2,-1]
def swapEnds(numbers):
    first =  numbers[0]
    last =  numbers[-1]
    numbers[-1] = first
    numbers[0] = last
    #numbers[0] = numbers[-1]#[len(numbers) -1]

# hasWildcat("kitty") -> false
# hasWildcat("tomcat") -> true
# hasWildcat("c4tn1P") -> true
def hasWildcat(word): # A-- would not buy again
    for index in range(len(word) -2):
        if word[index] == "c" and word[index+2] == "t":
            return True
    return False

# sumDigits(1234) -> 10
# sumDigits(1000) -> 1
# sumDigits(-581) -> 14
def sumDigits(num):
    total = 0
    num = +num
    while num != 0:
        total += num % 10
        num = num // 10
    
    """
    num = str(num)
    if num[0] == "-":
        num =  num[1:]
    for digit in num:
        total += int(digit)
    """
    return total


print(hasWildcat("kitty"))

print(maxMinDiff([-1,-100,12,2,100]))
#dates, highs, lows = readFile("temperatures.csv")