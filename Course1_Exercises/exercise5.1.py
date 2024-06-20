small = None
maxi = None
while True:
    rawstr = input('Enter a number: ')
    if rawstr == 'done':
        break
    else:    
        try: 
            no = int(rawstr)
        except:
            print('Invalid input')
            continue
        if small is None:
            small = no
        elif no < small:
            small = no
        if maxi is None:
            maxi = no
        elif no > maxi:
            maxi = no 
print ('maximum is ',maxi)
print ('minimum is ',small)
            
            


    