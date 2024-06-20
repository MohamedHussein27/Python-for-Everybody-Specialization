score = input('Enter Score:')
try:
    score = float(score)   
except:
    print('Error not a number')
    quit()
if score > 1 or score < 0:
        print('not a valid range')
else:
    if score >= 0.9 :
        grade = 'A'
    elif score < 0.9 and score >= 0.8 :
        grade = 'B' 
    elif score < 0.8 and score >= 0.7 :
        grade = 'C' 
    elif score < 0.7 and score >= 0.6 :
        grade = 'D' 
    elif score < 0.6 :
        grade = 'F'
    print(grade)   
