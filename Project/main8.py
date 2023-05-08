import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
z = 'insert into PURCHASE(id,store_name,product_name,color,quantity,purchase_amount,purchase_date) values(%s,%s,%s,%s,%s,%s,%s)'
a = [(1, 'MyKids', 'Toy Car', 'Red', 50, 500, '01-05-23'),(2, 'MyKids', 'Toy Train', 'Green', 25, 250, '01-05-23'),(3, 'ORay', 'Shirt', 'Blue',10,200,'01-05-23')]
cur.executemany(z,a)
mydb.commit()
print("Data inserted succesfully")