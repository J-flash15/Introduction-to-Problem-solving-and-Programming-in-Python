#shamar Gordon
#Oct 26, 2022
#Hawaiian Word Pronouncer




from multiprocessing.connection import answer_challenge


consonants  = ["h","w"]

 #left is the key and the right is the values

vowels = {"a":"AH-", "e": "EH-", "i" : "EE-", "o" : "OH-", "u" : "OO-"}
doubleVowels = {"ai": "EYE-", "ae" : "EYE-", "ao" : "OW-", "au" :"OW-",
 "\n" "ei" : "-AY-", "eu" : "-EH-OO-", "iu" : "-EW-", "oi" : "-OY-", "ou" : "-OW-", "ui" : "-OOEY-" }

valid = ['a', 'e','i', 'o', 'u', 'p', 'k', 'h','l','m', 'n', 'w', ' ','\'' ]


def validate(word):
   
    for letter in word:

        letter = letter.lower()

        if letter not in valid:

             return False               
            
    return True

def pronounce(word):

    i = 1 

    while i < len(word):
         

        #Check if the char is W and char come before is e or i  
        if word[i] == "W" and (word[i-1] == "e" or word[i-1] == "i" ):

            word = word[0:i] + "v" + word[i+1:]
        
        i = i +1 


    starttwoch = 0 

    endtwoch = 2

    

    while endtwoch < len(word):

         

        twoCh = word[starttwoch:endtwoch]

        if twoCh in doubleVowels.keys():

            startword = word[0:starttwoch]

            endword =  word[endtwoch:]
            
            pronouncedoubleVowel = doubleVowels[twoCh]


            word = startword + pronouncedoubleVowel + endword

        starttwoch = starttwoch + 1 

        endtwoch = endtwoch + 1

        

    index = 0 

    while index < len(word):


        ch = word[index]

        if ch in vowels.keys():

            startword = word[0:index]

            endword =  word[index+1:]
            
            pronounceVowel = vowels[ch]


            word = startword + pronounceVowel + endword


        index  = index + 1 

    return word

useresponse = True


while (useresponse == True):

    word = str(input("Enter a hawaiian word to pronounce ==>  "))
    word = word.lower()

    if(validate(word)== True):  

        Hawaiian = pronounce(word) 
        Hawaiian = Hawaiian.strip("-").lower()
        print(Hawaiian)

        vaildanswer = False

       #vaild answer check if its yes or no 
        while(vaildanswer == False):

            Answer  = input("Do you want to enter another word? Y/YES/N/NO ==> ") 

            Answer = Answer.upper()

            if (Answer == "N" or Answer == "NO"):

                useresponse = False

                vaildanswer = True

            elif(Answer == "Y" or Answer == "YES"):
                
                vaildanswer = True

                useresponse = True

            else: 

                print("Enter Y, YES, N or NO")

            
      

    else: 

        for letter in word:

            vaildCh = validate(letter) 
        
            if vaildCh == False: 

                print(letter + " is not a vaild hawaiian character")
            
                break

    






        
        
    
   

        
       
    

   





        



  
