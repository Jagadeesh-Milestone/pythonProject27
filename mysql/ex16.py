#update table:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='milestone3'
)
mycursor=mydb.cursor()
#sql="UPDATE users SET address='mumbai' WHERE address='chennai'"
sql="UPDATE users SET name='Jagadeesh' WHERE name='jagadeesh kumar'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,'records updated')