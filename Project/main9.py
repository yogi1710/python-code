import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
z = 'insert into SALE(id,store_name,product_name,color,no_of_items,sale_amount,sale_date) values(%s,%s,%s,%s,%s,%s,%s)'
a = [(1, 'Offline', 'Toy Car', 'Green', 100, 800, '2023-04-05'),
(2, 'Online', 'Toy Train', 'Green', 100, 800, '2023-01-05'),
(3, 'Offlin', 'Wooden Chair', 'Green', 100, 800, '2023-04-10'),
(4, 'Online', 'Wooden Table', 'Green', 100, 800, '2023-03-15'),
(5, 'Offline', 'Toy Train', 'Green', 100, 800, '2023-09-25')]
cur.executemany(z,a)
mydb.commit()
print("Data inserted succesfully")