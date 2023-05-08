#qus 8
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
update_manufacure ="UPDATE manufacture SET quantity = '50' WHERE color = 'Red'"
cur.execute(update_manufacure)  
show_manufacture= "select * from manufacture"
cur.execute(show_manufacture)  
print("Success")

