data = open("Dracula.txt","r")

text = data.read()

lines = text.split("\n")

totalVamp = 0

for l in lines:

    l = l.lower()

    numVamp = l.count("dracula")


    totalVamp = totalVamp + numVamp

    
print(totalVamp)


            
