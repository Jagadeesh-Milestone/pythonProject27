#select records from table
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='milestone3'
)
mycursor=mydb.cursor()
mycursor.execute('SELECT * FROM users')#for all columns
mycursor.execute('SELECT id,address FROM users')#for selected columns
result=mycursor.fetchall()
for i in result:
    print(i)
