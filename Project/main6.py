import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
z = 'insert into MANUFACTURE(id,product_name,color,quantity,manufacturing_date,defective_ITEM) values(%s,%s,%s,%s,%s,%s)'
a = [(1, 'Toy Car', 'Red', 100, '01-05-23', 0),(2, 'Toy Train', 'Green', 50, '01-05-23', 0),(3, 'Wooden Chair', 'Brown', 200, '01-04-23', 0),(4, 'Wooden Table', 'Brown', 100, '01-03-23', 0)]
cur.executemany(z,a)
mydb.commit()
print("Data inserted succesfully")