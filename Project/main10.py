#qus 7
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
dlelte_oray ="DELETE FROM purchase WHERE product_name = 'shirt' AND store_name = 'ORay' AND purchase_date = '2001-05-23'"
cur.execute(dlelte_oray)  
show_purchase = "select * from purchase"
cur.execute(show_purchase)  
print("Success")