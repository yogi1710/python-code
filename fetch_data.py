import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Yogeshwar@123',
    database = 'YOGI'
)
cur=mydb.cursor()
f = 'select * from YOGI'
cur.execute(f)
display = cur.fetchall()
for x in display:
    print(x)