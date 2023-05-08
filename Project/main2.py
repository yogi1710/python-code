import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
t = 'create table MANUFACTURE(id INTEGER(10) PRIMARY KEY,product_name VARCHAR(20),color VARCHAR(10),quantity INTEGER(10),manufacturing_date DATE,defective_ITEM VARCHAR(10))'
cur.execute(t)
print("Table created succesfully")