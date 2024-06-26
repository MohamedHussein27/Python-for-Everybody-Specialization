import re

opened = open('actual_data.txt')

count = 0
for line in opened:
    line = line.rstrip() #strip the right whitespace in each line
    list1 = re.findall('[0-9]+',line)  #taking all the integers in each line putting them into a list
    for no in list1:
        no = int(no) #convert string to integer
        count = count + no

print(count)