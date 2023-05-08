import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
t = 'create table PURCHASE(id INTEGER(10),store_name TEXT,product_name varchar(10),color VARCHAR(10),quantity INTEGER(10),purchase_amount INTEGER(20),purchase_date DATE)'
cur.execute(t)
print("Table created succesfully")