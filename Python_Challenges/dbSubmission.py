import sqlite3

# List of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Connect to a SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('files.db')

# Create a cursor object to execute SQL commands
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName \
        )")

# Filter the list to include only .txt files
txt_files = [file for file in fileList if file.endswith('.txt')]

# Insert the .txt files into the database
for file in txt_files:
    cur.execute('INSERT INTO tbl_files (col_filename) VALUES (?)', (file,))

# Commit the transaction
conn.commit()

# Fetch and print the .txt files from the database
cur.execute('SELECT * FROM tbl_files')
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
