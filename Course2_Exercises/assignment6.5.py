text = "X-DSPAM-Confidence:    0.8475"
startpos = text.find(' ')     # determine the position of the first space in the text
#print(startpos)              print it to know it
spaceoff = (text[startpos:]).lstrip()     # (text[startpos:]) >>> is to extract text from the position of the first space to the end of the original texxt, and then remove the left space from that text
final = float(spaceoff)   
type(final)           # make sure that you are doing right
print(final)