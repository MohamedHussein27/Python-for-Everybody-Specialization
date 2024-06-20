fname = input("Enter file name:")
opened = open(fname)
summation = 0
count = 0
for line in opened :
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        summation = summation + float(line[-6:])        #the number in the confidence line has 6 digits(4decimal places) so that's why I typed -6 to the end  
                                                        #cont. : and we already removed the space from the line so it's correct
        count = count + 1                                                #the count to get the no. of the points
print ("Average spam confidence:",summation/count)                                #printing the average of the decimal points