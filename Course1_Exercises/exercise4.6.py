def computepay():
    hrs = float(input('Enter Hours:'))
    r = float(input('Enter Rate:'))
    if hrs > 40 :
        pay = hrs*r
        ext = (hrs-40)*(.5)*r
        pay = pay + ext
    else:
        pay = hrs*r
    return pay    

p = computepay()
print('pay',p)