from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read() # Open the URL and read its contents into the 'html' variable
soup = BeautifulSoup(html, "html.parser")

count = 0
summation =  0

# Retrieve all of the anchor tags
tags = soup('span') # Retrieve all of the <span> tags in the HTML document
#print(tags)
for tag in tags:
    print('TAG:', tag)
    y = int(tag.string) # Convert the content of the <span> tag to a string and then to an integer
    count = count + 1
    summation = summation + y
print('Count:', count)  
print('Summation:', summation)  

