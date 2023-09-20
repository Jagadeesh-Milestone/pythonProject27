#create a table:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='milestone3'
)
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE employee(name VARCHAR(20),address VARCHAR(20))')
print('one table created successfully')