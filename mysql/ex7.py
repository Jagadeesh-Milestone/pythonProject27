#primary key
#every table must have a primary key
#it is used to create unique id for every record.
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='milestone3'
)
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE users(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), address VARCHAR(20)) ')
