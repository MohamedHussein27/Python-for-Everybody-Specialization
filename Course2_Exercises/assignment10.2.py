fname = input("Enter file name:")
opened = open(fname)

hours =  list() #making an empty list to put the desired hours into
counts = dict()  #making an empty dictionary to know how many times the sender sent emails
for line in opened:
    line = line.rstrip()
    if (line.startswith('From '))==1: #taking only emails form the lines stast with "From "
        stuff1 = line.split() #stuff1 is the whole line begins with "From " and now we have the list of emails
        #print (stuff1)
        stuff2 = stuff1[5].split(":") #stuff2 contains the  [hour, minute, second]
        hours.append(stuff2[0]) #hours is a list containing the hours only  

for hour in hours:
    counts[hour] = counts.get(hour,0) + 1 #if the hour is not in the dictionary then it will be added to the dictionary with the value 0 and if the hour is already in the dictionary then it will be added 1 to the value of that hour

for k,v in sorted(counts.items()):
    print(k,v) #printing the hour and the no. of emails sent at that hour with sorted order