import mysql.connector
mydb = mysql.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123'
)
print(mydb.connection_id)