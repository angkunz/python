import sqlite3
conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Angkun_python\example1.db")
c = conn.cursor()

try :
    data = ('A','X','CD@gmail.com','1')
    c.execute(''' UPDATE users SET fnme =?,IName =?,email =? WHERE id =?''',data)
    conn.commit ()
    result = c.fetchall()
    for x in result :
        print(x)
    c.close

except sqlite3.Error as e :
    print(e)

finally :
    if conn :
        conn.close ()