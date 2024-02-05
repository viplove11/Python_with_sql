# importing the python mysql connector module to connect both of them
import mysql.connector as myConnect

# creating connection
connection = myConnect.connect(host="localhost",user="root", password="root")

# checking for connection , it it is connected
if connection.is_connected():
    print("Connection successfull")

# creating the cursor object to execute queries
cursorObject = connection.cursor()

# query for showing the databases
cursorObject.execute("show databases")

# print the database available 
for db in cursorObject:
    print(db)

# creating new database called sampleData
query = "create database sampledata"
cursorObject.execute(query)

# showing updated databases list
print("Showing updated list: ")
cursorObject.execute("show databases")
for db in cursorObject:
    print(db)

connection.commit()