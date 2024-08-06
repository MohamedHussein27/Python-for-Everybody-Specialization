import json
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup by creating fresh tables
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER PRIMARY KEY,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'   # the name is roster_data.json only

# Sample JSON data format:
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

# Read the JSON data from the file
str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]    # Extract name from the JSON entry
    title = entry[1]   # Extract course title from the JSON entry
    role = entry[2]    # Extract role (1 for teacher, 0 for student) from the JSON entry

    print((name, title, role))

    # Insert the user into the User table, ignoring duplicates
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', (name,))
    
    # Retrieve the user_id of the inserted or existing user
    cur.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = cur.fetchone()[0]  # get user_id

    # Insert the course into the Course table, ignoring duplicates
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', (title,))
    
    # Retrieve the course_id of the inserted or existing course
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title,))
    course_id = cur.fetchone()[0]  # get course_id

    # Insert the membership record into the Member table
    cur.execute('''INSERT OR IGNORE INTO Member
        (user_id, course_id, role) VALUES (?,?,? )''',
        (user_id, course_id, role))  # place user_id, course_id, and role 

# Commit the changes to the database
conn.commit()
