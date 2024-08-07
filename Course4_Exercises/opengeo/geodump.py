# Import necessary libraries
import sqlite3
import json
import codecs

# Connect to the SQLite database (creates the database if it doesn't exist)
conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

# Select all rows from the Locations table
cur.execute('SELECT * FROM Locations')

# Open a new JavaScript file to write the data
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")

count = 0  # Counter for the number of records written

# Iterate over each row in the result set
for row in cur:
    data = str(row[1].decode())  # Decode the geodata from bytes to string
    try:
        js = json.loads(str(data))  # Parse the JSON data
    except:
        continue  # Skip the row if JSON parsing fails

    if len(js['features']) == 0:
        continue  # Skip if there are no features in the JSON data

    try:
        # Extract latitude, longitude, and display name from the JSON data
        lat = js['features'][0]['geometry']['coordinates'][1]
        lng = js['features'][0]['geometry']['coordinates'][0]
        where = js['features'][0]['properties']['display_name']
        where = where.replace("'", "")  # Remove single quotes from the display name
    except:
        print('Unexpected format')
        print(js)  # Print the JSON data for debugging
        continue

    try:
        print(where, lat, lng)  # Print the extracted data for verification

        count = count + 1  # Increment the counter
        if count > 1:
            fhand.write(",\n")  # Add a comma and newline for all but the first record

        # Create the output string in the format [lat, lng, 'where']
        output = "[" + str(lat) + "," + str(lng) + ", '" + where + "']"
        fhand.write(output)  # Write the output string to the JavaScript file
    except:
        continue  # Skip if there is any error in writing the data

fhand.write("\n];\n")  # Close the JavaScript array
cur.close()  # Close the database cursor
fhand.close()  # Close the JavaScript file

print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
