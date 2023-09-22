#limit the result:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='milestone3'
)
mycursor=mydb.cursor()
#mycursor.execute("SELECT * FROM users LIMIT 3")
mycursor.execute("select * FROM users LIMIT 3 OFFSET 2")
result=mycursor.fetchall()
for i in result:
    print(i)
