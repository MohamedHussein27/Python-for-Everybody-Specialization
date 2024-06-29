import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
print('retreive', url)
uh = urllib.request.urlopen(url, context=ctx) # Open the URL with the custom SSL context that skips verification

data = uh.read()  # Read the entire response data from the URL

tree = ET.fromstring(data) # Create the input tree structure
lst = tree.findall('comments/comment')  # getting all the comment tags

summation = 0
repeats = 0
for item in lst:
    count = item.find('count').text #get the number in the "comment" tags
    count = int(count)
    summation = count + summation  # Add the counts to get the sum
    repeats = repeats + 1 #get the no. of counts
print ('count:',repeats)
print('sum', summation)    