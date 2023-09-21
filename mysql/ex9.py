#insert multiple records
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='milestone3'
)
mycursor=mydb.cursor()
sql='INSERT INTO users (name,address) VALUES(%s,%s)'
values=[('naresh','hyderabad'),('suresh','chennai'),
        ('mahesh','chennai'),('jagadeesh kumar','bangalore'),
        ('satheesh kumar','hyderabad')]
mycursor.executemany(sql,values)
mydb.commit()
print(mycursor.rowcount,'records inserted into table')