#show tables
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='milestone3'
)
mycursor=mydb.cursor()
mycursor.execute('SHOW TABLES')
for i in mycursor:
    print(i)

