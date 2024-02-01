import mysql.connector as mysql
con=mysql.connect(host='localhost',user='root',passwd='',database='amazon')
cursor=con.cursor()
cursor.execute('select *   from customer')
rows=cursor.fetchall()
for i in rows:
    print('customer ID:',i[0])
    print('customer Name:',i[1])
    print('gender:', i[2])
    print('mobile number:', i[3])
    print('email ID:', i[4])