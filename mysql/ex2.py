#mysql
#mysql is a database which is used to store the data
#mysql is very familiar to python

import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha'
)
print('connected to mysql successfully')