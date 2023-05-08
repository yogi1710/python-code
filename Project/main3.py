import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
t = 'create table GOODS(id INTEGER(10),product_name varchar(10),color varchar(10),quantity INTEGER(10),manufacturing_date date)'
cur.execute(t)
print("Table created succesfully")