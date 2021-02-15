import sqlite3
"""conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Angkun_python\example.db")
c = conn.cursor() #create a cursor object 
c.execute ('''CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT,
    fnme varchar(30) NOT NULL,
    IName varchar(30) NOT NULL,
    email varchar(100) NOT NULL)''')
c.execute('''INSERT INTO users (id,fnme,IName,email) VALUES (NULL,"Akaradech","Thongngam","atstampzaza")''')
c.execute('''INSERT INTO users VALUES (NULL,"dodd","dukdik","dodikza")''')
conn.commit() #save (commit) the change
conn.close() #close the connecton when done"""

def insertTousers(fnme,IName,email):
    try :
        conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Angkun_python\example.db")
        c = conn.cursor()
        sql = '''INSERT INTO users (fnme,IName,email) VALUES (?,?,?)'''
        data = (fnme,IName,email)
        c.execute(sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
insertTousers("Guido","Rossum","python@gmail.com")
insertTousers("Dennis","Ritchie","abc")"""