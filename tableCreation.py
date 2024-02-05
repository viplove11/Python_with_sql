import mysql.connector as connector

connection = connector.connect(host="localhost",user="root",password="root",database="sampledata")

if connection.is_connected():
    print("Connection successfull")


cursorObject = connection.cursor()

# using sample database query
query = "use sampledata"
cursorObject.execute(query)

# query for creating student table if it does not exists
query = "create table if not exists student(name varchar(90) NOT NULL, age int NOT NULL, city varchar(90) NOT NULL,marks int NOT NULL)"

cursorObject.execute(query)

# showing table student after creating it
print("Showing tables in sampledata datbase: ")
query ="show tables"
cursorObject.execute(query)

for tables in cursorObject:
    print(tables)

    