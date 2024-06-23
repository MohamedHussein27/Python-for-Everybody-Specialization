fname = input("Enter file name:")
opened = open(fname)

count = 0
for line in opened:
    line = line.rstrip()
    if (line.startswith('From:'))==1:
        count = count + 1   #counter to count the number of lines started with 'From:'
        stuff = line.split()
        print(stuff[1])
print ("There were",count, "lines in the file with From as the first word")