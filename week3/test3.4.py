a = []
while True :
    b = input('----ร้านล้าน----\n เพิ่ม\t\t[a]\n แสดง\t\t[s]\n ออกจากระบบ\t[x]\n')
    b = b.lower()
    if b == 'a' : 
        c = input('ป้อนรายชื่อลูกค้า(รหัส : ชื่อ : จังหวัด)')
        a.append(c)
        print('\n*******ข้อมูลได้เข้าสู่ระบบแล้ว*******\n')
    elif b == 's' : 
        print('{0:-<30}'.format(""))
        print('{0:-<10}{1:-<15}{2:15}'.format('รหัส','ชื่อ','จังหวัด'))
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        for d in a : 
            e = d.split(":")
            print('{0[0]:<6} {0[1]:<10}({0[2]:<10})'.format(e))
            continue
    elif b == 'x' : 
        break
print('ทำคำสั่งถัดไป')