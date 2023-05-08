#qus 10
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
profit_margin ="SELECT margin FROM sale WHERE product_name = 'wood table' AND store_name = 'Mykids' AND manufacture_id IN (  SELECT manufacture_id  FROM manufacture  WHERE company_name = 'SS Export')"
cur.execute(profit_margin)
print("Success")

