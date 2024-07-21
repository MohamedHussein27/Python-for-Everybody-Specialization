<<<<<<< HEAD
import urllib.request, urllib.parse, urllib.error
import json, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
print('retreiving', url)
uh = urllib.request.urlopen(url, context=ctx) # Open the URL with the custom SSL context that skips verification

data = uh.read()  # Read the entire response data from the URL
js = json.loads(data) # shows data as a json object

count = len(js["comments"])  #getting the the number of comments in the comments list
print('Count:', count)

summation = 0

for i in range(count): #iterate over the comments list by the number of elements it has
    summation += js["comments"][i]["count"]  #summing up all the counts ( summing the values with the key count in all the list dictionaries)
print('Sum:', summation)
=======
import urllib.request, urllib.parse, urllib.error
import json, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
print('retreiving', url)
uh = urllib.request.urlopen(url, context=ctx) # Open the URL with the custom SSL context that skips verification

data = uh.read()  # Read the entire response data from the URL
js = json.loads(data) # shows data as a json object

count = len(js["comments"])  #getting the the number of comments in the comments list
print('Count:', count)

summation = 0

for i in range(count): #iterate over the comments list by the number of elements it has
    summation += js["comments"][i]["count"]  #summing up all the counts ( summing the values with the key count in all the list dictionaries)
print('Sum:', summation)
>>>>>>> f71ec42ed1a662331aa8a68293b5cffdff3f6c71
