#filter records
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='milestone3'
)
mycursor=mydb.cursor()
#mycursor.execute("SELECT * FROM users WHERE address='bangalore'")
#mycursor.execute("SELECT * FROM users WHERE name='hari'")
#mycursor.execute("SELECT * FROM users WHERE name LIKE '%kumar%'")
mycursor.execute("SELECT * FROM users WHERE address like'%gal%'")
result=mycursor.fetchall()
for i in result:
    print(i)