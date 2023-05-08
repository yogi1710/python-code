#qus 9
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
display_wooden ="SELECT *FROM goods WHERE product_name = 'wood chair' AND manufacturing_date < '2001-05-23'"
cur.execute(display_wooden)  
print("Success")

