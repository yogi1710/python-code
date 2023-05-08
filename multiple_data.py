import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'YOGI'
)
cur=mydb.cursor()
z = 'insert into yogi(emp_id,emp_name,salary) values(%s,%s,%s)'
a = [(101,'tarak',35000),(102,'hari',30000),(103,'suresh',40000)]
cur.executemany(z,a)
mydb.commit()
print("Data inserted succesfully")
