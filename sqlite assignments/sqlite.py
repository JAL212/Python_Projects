import sqlite3

#from previous challenges, to create table
connection = sqlite3.connect("C:/Users/lapin/My_Documents/GitHub/Python_Projects/Python_Projects/sqlite assignments/test_database.db")
c = connection.cursor()
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
connection.commit()

#get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

#execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
    c.execute(line)
