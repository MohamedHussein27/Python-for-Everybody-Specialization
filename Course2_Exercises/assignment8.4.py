fname = input("Enter file name:")
opened = open(fname)

stuff = list() #creating empty list to do work on

for line in opened:
    splitted = line.split() #split the words of each line
    for word in splitted:
        if word in stuff:
            continue 
        stuff.append(word) #if the word is not new to the list then put it in the list

stuff.sort() #sorting the list alphabetically

print(stuff)