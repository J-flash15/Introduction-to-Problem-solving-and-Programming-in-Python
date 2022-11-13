from ast import While
import random
from re import X
from unittest import result

def roll():
    return random.randint(1,6)
def autoPig():
    total = 0
    done = False

    #and not done == True  
    while total < 20 and not done:
        result =  roll()
        # print("Roll:", result)

        #Done becomes True but not True beomes False and that happnes when you roll A 1
        if result == 1:
            total = 0
            done = True
        else:


            #this is for the players point and their current turn 
            total += result  
    # print("Turn Total:", total)
    # print("...")
    return total
    

def holdAt20(trials):
    outcomes = {}
    for _ in range(trials):
        turnTotal = autoPig()
        if turnTotal in outcomes:
            outcomes[turnTotal] +=1
        else:
            outcomes[turnTotal] = 1
    for turnTotal in sorted(outcomes):
        print(turnTotal, "\t", outcomes[turnTotal]/trials)
Hold = int(input("how many Hold-at-20 turn simulations: "))
print("Score \t Estimated Probability")



holdAt20(Hold)


def holdAtX(trials, X):
    outcomes = {}
    for _ in range(trials):
        turnTotal = autoPigX(X)
        if turnTotal in outcomes:
            outcomes[turnTotal] +=1
        else:
            outcomes[turnTotal] = 1
    for turnTotal in sorted(outcomes):
        print(turnTotal, "\t", outcomes[turnTotal]/trials)
Hold = int(input("how many Hold-at-X turn simulations: "))
print("Score \t Estimated Probability")

def autoPigX(X):
    total = 0
    done = False

    #and not done == True  
    while total < X and not done:
        result = roll()
        #print("Roll:", result)

        #Done becomes True but not True beomes False and that happnes when you roll A 1
        if result == 1:
            total = 0
            done = True
        else:


            #this is for the players point and their current turn 
            total += result  
    # print("Turn Total:", total)
    # print("...")

    return total

holdAtX(1000, 100)


def holdAt20orGoal(playerscore):

    turnTotal = autoPigGoal(playerscore)

    print("New Score: ", playerscore+turnTotal)
    




def autoPigGoal(playerscore):
    total = 0
    done = False

    #and not done == True  
    while (total < 20 and playerscore + total <=100)  and not done:
        result = roll()
        print("Roll:", result)

        #Done becomes True but not True beomes False and that happnes when you roll A 1
        if result == 1:
            total = 0
            done = True
        else:


            #this is for the players point and their current turn 
            total += result  
    print("Turn Total:", total)
    # print("...")

    return total

playerscore = int(input("score ? "))

holdAt20orGoal(playerscore)

'''def holdAt20orGoalGame():
    outcomes = {}
    for _ in range(trials):
        turnTotal = autoPig()
        if turnTotal in outcomes:
            outcomes[turnTotal] +=1
        else:
            outcomes[turnTotal] = 1
    for turnTotal in sorted(outcomes):
        print(turnTotal, "\t", outcomes[turnTotal]/trials)
'''