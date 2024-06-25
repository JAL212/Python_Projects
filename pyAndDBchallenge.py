import sqlite3

# Create a database in RAM
connection = sqlite3.connect(':memory:')

# Create a cursor object
cursor = connection.cursor()

# 1. Create a table named Roster with fields 'Name', 'Species', and 'IQ'
cursor.execute('''
    CREATE TABLE Roster (
        Name TEXT,
        Species TEXT,
        IQ INTEGER
    )
''')

# 2. Populate the table with the provided values
roster_data = [
    ('Jean-Baptiste Zorg', 'Human', 122),
    ('Korben Dallas', 'Meat Popsicle', 100),
    ('Ak\'not', 'Mangalore', -5)
]

cursor.executemany('''
    INSERT INTO Roster (Name, Species, IQ)
    VALUES (?, ?, ?)
''', roster_data)

# 3. Update the Species of Korben Dallas to be Human
cursor.execute('''
    UPDATE Roster
    SET Species = 'Human'
    WHERE Name = 'Korben Dallas'
''')

# 4. Display the names and IQs of everyone in the table who is classified as Human
cursor.execute('''
    SELECT Name, IQ
    FROM Roster
    WHERE Species = 'Human'
''')

# Fetch and print the results
human_roster = cursor.fetchall()
for person in human_roster:
    print(f'Name: {person[0]}, IQ: {person[1]}')

# Commit the changes and close the connection
connection.commit()
connection.close()
