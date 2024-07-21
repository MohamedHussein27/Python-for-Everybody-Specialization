import sqlite3

conn = sqlite3.connect('Counting_Organizations.sqlite') # Connect to the SQLite database (or create it if it doesn't exist)
cur = conn.cursor() # Create a cursor object to interact with the database

cur.execute('DROP TABLE IF EXISTS Counts') # Delete the table Counts to begin the whole process
cur.execute('''
    CREATE TABLE Counts (org TEXT, count INTEGER)''') # Create a new table named Counts with two columns: org and count

fname = input('Enter file name:') # Prompt the user to enter the file name
if (len(fname) < 1): fname = 'mbox-short.txt' # If the file name is empty, use the default file 'mbox-short.txt'
fh = open(fname) # Open the file for reading
line_count = 0 # Initialize a counter to keep track of the number of lines processed
for line in fh: # Iterate through each line in the file
    if not line.startswith('From: '): continue # Skip lines that do not start with 'From: '
    pieces = line.split() # Split the line into words
    email = pieces[1] # The email address is the second word in the line
    org = email.split('@')[1] # Extract the organization from the email address by splitting at '@' and taking the domain part
                              #the email for ex is like : (username)@(domain name) so by this line we will get the domain name which is the organization
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,)) # Query the database to see if the organization is already in the table
    row = cur.fetchone() # Fetch the first result from the query
    line_count = line_count + 1 # Increment the line counter
    if row is None: # If the organization is not found in the table
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,)) # Insert the organization with a count of 1
    else: # If the organization is found in the table
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,)) # Update the count by incrementing it by 1
conn.commit() # Commit the changes to the database and I made it outside the loop as it takes much time

sqlstr = 'SELECT org , count FROM Counts ORDER BY count DESC LIMIT 10' # SQL query to select the top 10 organizations by count, in descending order

for row in cur.execute(sqlstr): # Execute the query and iterate through the results
    print(str(row[0]), row[1]) # Print the organization and its count

cur.close() # Close the cursor
