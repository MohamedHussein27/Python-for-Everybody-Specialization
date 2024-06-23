fname = input("Enter file name:")
opened = open(fname)

emails =  list() #making an empty list to put the desired emails into
counts = dict()  #making an empty dictionary to know how many times the sender sent emails
for line in opened:
    line = line.rstrip()
    if (line.startswith('From:'))==1: #taking only emails form the lines stast with "From:"
        stuff = line.split()
        emails.append(stuff[1])  #stuff[1] is the email and now we have the list of emails

for email in emails:
    counts[email] = counts.get(email,0) + 1 #if the email is not in the dictionary then it will be added to the dictionary with the value 0 and if the email is already in the dictionary then it will be added 1 to the value of that email

BigKey = None
BigValue = None
for key,value in counts.items(): #Gitting the email with the greatest value
    if BigValue is None or value > BigValue:
        BigKey = key
        BigValue = value

print(BigKey,BigValue)        