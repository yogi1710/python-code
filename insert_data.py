import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'YOGI'
)
cur=mydb.cursor()
z = 'insert into yogi(emp_id,emp_name,salary) values(%s,%s,%s)'
a = (100,'Yogi',25000)
cur.execute(z,a)
mydb.commit()
print("Data inserted succesfully")
