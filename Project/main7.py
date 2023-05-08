import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
z = 'insert into GOODS(id,product_name,color,quantity,manufacturing_date) values(%s,%s,%s,%s,%s)'
a = [(1, 'Toy Car', 'Red', 100, '01-05-23'),(2, 'Toy Train', 'Green', 50, '01-05-23'),(3, 'Wood Chair', 'Brown', 200, '01-04-23'),(4, 'Wood Table', 'Brown', 100, '01-03-23')]
cur.executemany(z,a)
mydb.commit()
print("Data inserted succesfully")