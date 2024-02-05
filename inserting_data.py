import mysql.connector as connector

connection = connector.connect(host="localhost",user="root",password="root",database="sampledata")

if connection.is_connected():
    print("Connection successfull")


cursorObject = connection.cursor()

# using sample database query
query = "insert into student(name, age, city, marks) values ('viplove',23,'Pune',99),('Harsh',20,'Bilaspur',89)"
cursorObject.execute(query)

# displaying data from table
query ="select * from student"
cursorObject.execute(query)

for data in cursorObject:
    print(data)
    
connection.commit()