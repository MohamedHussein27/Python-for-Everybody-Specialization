from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url: ')
repeats = input('Enter Repeats: ')
repeats = int(repeats)
position = input('Enter Position: ')
position = int(position)
for repeat in range(repeats): #repeating the outer loop like clicking on the next name the required times
     html = urlopen(url, context=ctx).read() # Open the URL and read its contents into the 'html' variable
                                            # and every loop with a unique url
     soup = BeautifulSoup(html, "html.parser")
     tags = soup('a') # Retrieve all of the <a> tags in the HTML document
     count = 0
     for tag in tags:
        # Look at the parts of a tag
        url = tag.get('href', None) #gitteng the url
        name = tag.contents[0]  #getting the name
        count = count + 1
        if count == position: #if the position then break the inner loop to start the proccess again but with the last name and url
            break
print('name:', name)
print('url:', url)