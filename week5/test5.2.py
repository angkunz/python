import os as os
product = []
price = []
amount = []
class Shop :
    def power(self) :
        i = 0
        while i < 100 :
            a = 0
            amount.append(a)
            i+=1
    def create2(self) :
        location = 0
        while True :
            os.system('cls')
            print('เพิ่มรายการสินค้า หากต้องการยกเลิกกรอก exit')
            nameproduct = input('เพิ่มชื่อสินค้า :')
            if nameproduct == 'exit' :
                os.system('cls')
                break
            else :
                if nameproduct in product :
                    amountproduct = input('จำนวนสินค้า :')
                    location = product.index(nameproduct)
                    amount[location]+=int(amountproduct)
                else :
                    priceproduct = input('เพิ่มราคาสินค้า :')
                    amountproduct = input('จำนวนสินค้า :')
                    product.append(nameproduct)
                    price.append(priceproduct)
                    location = product.index(nameproduct)
                    amount[location]+=int(amountproduct)
            print('ทำรายการเสร็จสิ้น')
    def delete(self) :
        location = 0
        while True :
            os.system('cls')
            print('ลบรายการสินค้า กรอก exit เมื่อเสร็จสิ้น')
            deleteproduct = input('กรอกชื่อสินค้าที่ต้องการลบ : ')
            if deleteproduct == 'exit' :
                break
            else :
                if deleteproduct in product :
                    location = product.index(deleteproduct)
                    del amount[location]
                    del product[location]
                    del price[location]
                    os.system('cls')
                    print('ทำรายการเสร็จสิ้น')
                    q = input('ทำรายการต่อหรือไม่ (y/n) :')
                    if q.lower() == 'y' :
                        print('ทำรายการต่อ...')
                    else :
                        break
                else :
                    os.system('cls')
                    print('ไม่มีรายการสินค้านี้ กรุณาทำรายการใหม่')
                    q = input('ทำรายการต่อหรือไม่ (y/n) :')
                    if q.lower() == 'y' :
                        print('ทำรายการต่อ...')
                    else :
                        os.system('cls')
                        break
    def show(self) :
        os.system('cls')
        print("{0: <22}{1: <15}{2: <15} ".format('ชื่อสินค้า','ราคา','จำนวนสินค้า'))
        chak = len(product)
        if chak >= 1 :
            for r in range(chak) :
                print("{0: <20}{1: <15}{2: <10}".format(product[r], price[r], amount[r]))
            print('\n')
        else :
            print('ไม่มีรายการ\n\n')
x = Shop()
x.power()
while True :
    os.system('cls')
    print('กรุณาเลือกเมนู\n[a]เพื่อเพิ่มสินค้า\n[s]แสดงรายการสินค้า\n[d]ลบรายการสินค้า\n[x]ออกจากโปรแกรม')
    menu = input('เลือกเมนู : ')
    if menu == 'a' :
        x.create2()
    elif menu == 's' :
        x.show()
    elif menu == 'd' :
        x.delete()
    else :
        r = input('ต้องการออกจากโปรแกรมหรือไม่ (y/n) :')
        if r.lower() == 'y' :
            print('ขอบคุณที่ใช้บริการ...')
            break
        else :
            os.system('cls')