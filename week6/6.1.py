import sqlite3

conn = sqlite3.connect(r'C:\Users\qqx99\Documents\Angkun_python\datastudent.db')
c = conn.cursor()
# Create table

# c.execute("""CREATE TABLE students (id integer PRIMARY KEY AUTOINCREMENT,
#     fname varchar(30) NOT NULL,
#     lname varchar(30) NOT NULL,
#     email varchar(100) NOT NULL,
#     sex varchar(10) NOT NULL,
#     age varchar(10) NOT NULL,
#     year varchar(5) NOT NULL)""")
# conn.commit()
# conn.close()


def menu():
    global choice
    print('-'*5,'ระบบทะเบียนนักเรียน','-'*5)
    print('='*28,'\nเพิ่มข้อมูลนักเรียน กด [a]\nแสดงข้อมูลนักเรียน [s]\nแก้ไขข้อมูลนักเรียน [e]\nลบข้อมูลนักเรียน [d]\nออกจากระบบ [x]')
    choice = input('\nกรุณาเลือกทำรายการ :')

def add(fname,lname,email,sex,age,year):
    try :
        conn = sqlite3.connect(r'C:\Users\qqx99\Documents\Angkun_python\datastudent.db')
        c = conn.cursor()
        sql = '''INSERT INTO students (fname,lname,email,sex,age,year) VALUES (?,?,?,?,?,?)'''
        data = (fname,lname,email,sex,age,year)
        c.execute(sql,data)
        conn.commit()
        c.close()
        print('เพิ่มข้อมูลเรียบร้อย')

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()

def show():
    conn = sqlite3.connect(r'C:\Users\qqx99\Documents\Angkun_python\datastudent.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM students''')
    result = c.fetchall()
    print('{0:<12}{1:<15}{2:<15}{3:<27}{4:<6}{5:<6}{6}'.format('ลำดับที่',' ชื่อ','สกุล','อีเมล','เพศ','อายุ','ชั้นปี'))
    for x in result :
        print('{0:<8}{1:<15}{2:<15}{3:<27}{4:<6}{5:<6}{6}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
    print('ทำรายการเสร็จสิ้น\n')
    conn.commit()
    conn.close()

def edit(fname,lname,email,sex,age,year,iid):
    conn = sqlite3.connect(r'C:\Users\qqx99\Documents\Angkun_python\datastudent.db')
    c = conn.cursor()
    try :
        data = (fname,lname,email,sex,age,year,'{}'.format(iid))
        c.execute('''UPDATE students SET fname =?, lname =?, email =?, sex =?, age =?, year =? WHERE id = ?''',data)
        conn.commit()
        c.close()
        print('แก้ไขข้อมูลเรียบร้อย\n')
        
    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()

def delete(del_id):
    conn = sqlite3.connect(r'C:\Users\qqx99\Documents\Angkun_python\datastudent.db')
    c = conn.cursor()
    try :
        c.execute('DELETE FROM students WHERE id = {}'.format(del_id))
        conn.commit()
        c.close()
        print('ลบข้อมูลเรียบร้อย\n')       

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()

while True:
    menu()       
    if choice == 'a':
        fn,ln,em,s,a,y = input('ชื่อ-สกุล-อีเมล-เพศ-อายุ-ชั้นปี : ').split()
        add(fn,ln,em,s,a,y)
    elif choice == 's':
        show()
    elif choice == 'e':
        iid = input('เลือกลำดับที่ต้องการแก้ไข : ')
        efn,eln,eem,es,ea,ey = input('ชื่อ-สกุล-อีเมล-เพศ-อายุ-ชั้นปี : ').split()
        edit(efn,eln,eem,es,ea,ey,iid)
    elif choice == 'd':
        del_id = input('เลือกลำดับที่ต้องการลบ : ')
        delete(del_id)

    elif choice == 'x':
        yesno = input('ต้องการออกจากระบบหรือไม่ [y/n]: ')
        if yesno == 'Y' or yesno == 'y':
            print('ออกจากระบบเรียบร้อยแล้ว')
            break
        elif yesno == 'N' or yesno == 'n':
            print('ได้ทำการกลับสู่ระบบแล้ว')
            continue
        else:
            print('ทามรายย กดรายยอะ')
'''"""reset"""     
DELETE FROM students;
DELETE FROM sqlite_sequence WHERE name = 'students'
'''