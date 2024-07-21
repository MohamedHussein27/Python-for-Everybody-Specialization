import sqlite3

conn = sqlite3.connect('Counting_Organizations.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts') #deletes the table Counts to begin the whole process
cur.execute('''
    CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name:')
if (len(fname) < 1): fname = 'mbox-short.txt' #if file name has a zero chars then go to the mbox file
fh = open(fname)
line_count = 0 ;  
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1] #the email for ex is like : (username)@(domain name) so by this line we will get the domain name which is the organization
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    line_count = line_count + 1 #to count the no of the iteration
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
conn.commit() #outside the loop to be faster as the instruction commit takes mush

sqlstr = 'SELECT org , count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

cur.close()