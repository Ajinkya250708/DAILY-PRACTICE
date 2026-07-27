import mysql.connector as ms

con1 = ms.connect(host="localhost", database="Pikachu", user="root", password="Tiger")
cursor1 = con1.cursor()

cursor1.execute("create table newitems (itemno char(4), iname varchar(20), price float(5,2), category char(1));")

cursor1.execute("insert into newitems values('A101', 'Pencil', 1.50, 'A');")
cursor1.execute("insert into newitems values('A101', 'Pen', 10.00, 'A');")
cursor1.execute("insert into newitems values('B101', 'Copy', 20.00, 'B');")
cursor1.execute("insert into newitems values('C101', 'Ruler', 5.50, 'C');")
cursor1.execute("insert into newitems values('C101', 'Sharpner', 3.00, 'C');")
con1.commit()

cursor1.execute("select * from newitems;")
rs = cursor1.fetchall()
n = cursor1.rowcount
print("Total number of records=", n)

for i in range(n):
    print(rs[i])

cursor1.close()   
con1.close()       