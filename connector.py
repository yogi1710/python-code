import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'YOGI'
)
#print(mydb.connection_id)
cur=mydb.cursor()
#cur.execute('create database YOGI')
t = 'create table YOGI(emp_id integer(4),emp_name varchar(30),salary integer(10))'
cur.execute(t)
print("Table created succesfully")