import os as os
product = []
price = []
amount = []

def power() :
    i = 0
    global amount
    while i < 100 :
        a = 0
        amount.append(a)
        i+=1
def create2() :
    global product
    global price
    global amount
    location = 0
    while True :
        print('เพิ่มรายการสินค้า หากต้องการยกเลิกกรอก exit')
        nameproduct = input('เพิ่มชื่อสินค้า :')
        if nameproduct == 'exit' :
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
        os.system('cls')
        print('ทำรายการเสร็จสิ้น')

def delete() :
    global product
    global price
    global amount
    location = 0
    while True :
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
            else :
                os.system('cls')
                print('ไม่มีรายการสินค้านี้ กรุณาทำรายการใหม่')

def show() :
    global product
    global price
    global amount
    print("{0: <22}{1: <15}{2: <15} ".format('ชื่อสินค้า','ราคา','จำนวนสินค้า'))
    chak = len(product)
    if chak >= 1 :
        for r in range(chak) :
            print("{0: <20}{1: <15}{2: <10}".format(product[r], price[r], amount[r]))
    else :
        print('ไม่มีรายการ\n\n')

power()
while True :
    print('กรุณาเลือกเมนู\n[a]เพื่อเพิ่มสินค้า\n[s]แสดงรายการสินค้า\n[d]ลบรายการสินค้า\n[x]ออกจากโปรแกรม')
    menu = input('เลือกเมนู : ')
    if menu == 'a' :
        create2()
    elif menu == 's' :
        show()
    elif menu == 'd' :
        delete()
    else :
        break
#00000