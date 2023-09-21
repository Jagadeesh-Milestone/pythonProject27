#delete records
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='milestone3'
)
mycursor=mydb.cursor()
mycursor.execute('DELETE FROM users WHERE id=4')
#mycursor.execute("DELETE FROM users WHERE name='hari'")
#mycursor.execute("DELETE FROM users WHERE address='chennai'")

mydb.commit()


