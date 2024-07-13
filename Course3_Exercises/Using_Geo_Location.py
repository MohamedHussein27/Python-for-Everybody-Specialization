import urllib.request, urllib.parse, urllib.error
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    address = address.strip()
    parms = dict()
    parms['q'] = address  #q parameter which has the address

    url = serviceurl + urllib.parse.urlencode(parms) # adding the name of the location to the original url to liik in the location with the name provided
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()  #convert from UTF-8 to Unicode
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)  # shows data as a json object
    except:
        js = None
        print('There is no such a Location') # if wrong location
    #print(js)
    print(js['features'][0]['properties']['plus_code'])   #getting into data dictionary then to the value of the key "Features"
                                                          # and then to the value of the key "properties"
                                                          # and then to the value of the key "plus_code"
    