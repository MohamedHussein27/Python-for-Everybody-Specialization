import sqlite3

# Connect to SQLite database (creates the database file if it doesn't exist)
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()  # Create a cursor object to interact with the database

# Make some fresh tables using executescript()
# I added the Genre table
cur.executescript('''
DROP TABLE IF EXISTS Artist;  # Drop existing Artist table if it exists
DROP TABLE IF EXISTS Genre;  # Drop existing Genre table if it exists
DROP TABLE IF EXISTS Album;  # Drop existing Album table if it exists
DROP TABLE IF EXISTS Track;  # Drop existing Track table if it exists

# Create a new Artist table with unique IDs and unique names
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

# Create a new Genre table with unique IDs and unique names
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

# Create a new Album table with unique IDs, linked to the Artist table by artist_id
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

# Create a new Track table with unique IDs, linked to Album and Genre tables by album_id and genre_id
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Open the CSV file containing track data
handle = open('tracks.csv')

# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103,Rock
#   0                          1      2           3  4   5      6

# Read each line from the CSV file
for line in handle:
    line = line.strip()  # Remove leading and trailing whitespace
    pieces = line.split(',')  # Split the line by commas into a list of values
    if len(pieces) < 7: continue  # Skip lines with fewer than 7 elements (to account for Genre)

    # Extract each piece of data from the split line
    track_name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]  # I added this as the genre is on the 7th column

    print(track_name, artist, album, count, rating, length , genre)  # Print the parsed data for debugging

    # Artist part: Insert the artist name into the Artist table if it doesn't exist
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]  # Getting the artist id

    # Album part: Insert the album title and artist_id into the Album table if it doesn't exist
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]  # Getting the album id

    # Genre part: Insert the genre name into the Genre table if it doesn't exist
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]  # Getting the genre id

    # Track part: Insert or replace the track details into the Track table
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( track_name, album_id, genre_id, length, rating, count ) )  # Added genre_id and added one extra ? in the previous line
    
    conn.commit()  # Commit the transaction to save changes to the database
