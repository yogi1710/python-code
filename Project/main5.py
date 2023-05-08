import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
t = 'create table SALE(id INTEGER(10),store_name VARCHAR(10),product_name VARCHAR(20),color VARCHAR(10),no_of_items INTEGER(10),sale_amount REAL,sale_date DATE)'
cur.execute(t)
print("Table created succesfully")