# Import necessary libraries
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

# Service URL for the geocoding API
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Uncomment to enable HTTP debugging
# http.client.HTTPConnection.debuglevel = 1

# Connect to the SQLite database (creates the database if it doesn't exist)
conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

# Create the table if it doesn't exist
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Open the file containing addresses
fh = open("where.data")
count = 0  # Counter for the number of addresses processed
nofound = 0  # Counter for addresses not found

for line in fh:
    if count > 100:  # Stop after processing 100 addresses
        print('Retrieved 100 locations, restart to retrieve more')
        break

    address = line.strip()  # Get address from the file and strip any leading/trailing whitespace
    print('')

    # Check if the address is already in the database
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
                (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]  # Fetch geodata if the address is found
        print("Found in database", address)
        continue
    except:
        pass  # Address not found in database, proceed to fetch from API

    # Prepare parameters for the API request
    parms = dict()
    parms['q'] = address

    # Construct the full URL for the API request
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)  # Open the URL
    data = uh.read().decode()  # Read and decode the response
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))  # Print the first 20 characters of the response
    count = count + 1  # Increment the counter

    try:
        js = json.loads(data)  # Parse the JSON response
    except:
        print(data)  # Print the data in case of a parsing error
        continue

    # Check if the JSON response is valid and contains the expected data
    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    # Check if any features were found in the response
    if len(js['features']) == 0:
        print('==== Object not found ====')
        nofound = nofound + 1  # Increment the not found counter

    # Insert the address and geodata into the database
    cur.execute('''INSERT INTO Locations (address, geodata)
        VALUES ( ?, ? )''',
                (memoryview(address.encode()), memoryview(data.encode()) ))

    # Commit the transaction
    conn.commit()

    # Pause after every 10 addresses to avoid overwhelming the server
    if count % 10 == 0:
        print('Pausing for a bit...')
        time.sleep(5)

# Print the number of addresses that could not be found
if nofound > 0:
    print('Number of features for which the location could not be found:', nofound)

print("Run geodump.py to read the data from the database so you can visualize it on a map.")

# I add two new places to the where.data list:
# (City Stars Mall, Extension Makram Abaid Street, Cairo) 
# (British University in Egypt, Al Horeya Road, Cairo)
