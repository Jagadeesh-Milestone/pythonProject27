#create a new database
#to create a new database in mysql we use "CREATE DATABASE" statement
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha'
)
mycursor=mydb.cursor()
mycursor.execute('CREATE DATABASE milestone3')
print('database created successfully')
