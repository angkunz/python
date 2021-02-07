#import os 
price = [20,25,10,12,15,7]
wallet =['โออิชิ    ','อิชิตัน    ','M150    ','กระทิงแดง','เป็บซี่    ','น้ำเปล่า  ']
good = [0,0,0,0,0,0]
def product():
    print(" รายการสินค้า\n",20*"-")
    for i in range(6):
        print(i+1,".",wallet[i]," ราคา",price[i],"บาท")

def choose():
    for i in range(6):
        print(i+1,".",wallet[i]," ราคา",price[i],"บาท")
    data1 = int(input("กรุณาเลือกหยิบสินค้าหมายเลข :"))
    for i in range(6):
        if data1 == i+1:  
            good[i] +=1

def show():
    sumz = 0
    sumx = 0 
    print(" ___สินค้าของคุณที่หยิบมีดังนี้___\n----สินค้า",10*"-"+"จำนวน",7*"-"+"ราคา---")
    for i in range(6):
        sumz = sumz+good[i]
        sumx = sumx+(good[i]*price[i])
        if good[i] > 0:
            print(4*"-",wallet[i],6*"-",good[i],12*"-",good[i]*price[i])
    print("รวม",16*"-",sumz,12*"-",sumx)
while(True):
    print('-'*30)
    print("ร้าน Here Tu Shop")
    print('-'*30)
    print("1.แสดงรายการสินค้า\n2.หยิบสินค้าเข้าตะกร้า\n3.จำนวนและราคาสินค้าที่หยิบ\n4.ปิดโปรแกรม")
    data = int(input("กรุณาลือกทำรายการ"))
    if data == 1:
        product()
    elif data == 2 :
        choose()
    elif data == 3 : 
        show()
    else : 
        out = input("คุณต้องการออกจากโปรแกรมใช่ไหม (y / n) :")
        if out == "y" :
            print("ขอบคุณที่ท่านมาใช้บริการ")
            break