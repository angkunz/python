#22มกราคม2564
""" #โปรแกรมคิดค่าผ่านทาง
print("เลือกเมนูเพื่อทำรายการ")
print("#############################")
print("กด 1 เลือกแบบเหมาจ่าย")
print("กด 2 เลือกแบบจ่ายเพิ่ม")

manu= int(input("เลือก : "))

if manu == 1 : #แบบจ่ายเพิ่ม
    high= int(input("กรุณากรอกระยะทาง : "))
    if high<=25 :
        print("ค่าใช้จ่ายรวม 25 บาท") #ระยะทางไม่เกิน25กิโลเมตร
    else :
        print("ค่าใช้จ่ายรวม 55 บาท") #ระยะทางเกิน25กิโลเมตร
elif manu == 2 : 
    high= int(input("กรุณากรอกระยะทาง : "))
    if high < 25 :
        print("ค่าใช้จ่ายรวม 25 บาท") #ระยะทางไม่เกิน25กิโลเมตร
    else :
        print("ค่าใช้จ่ายรวม", int(25+55), "บาท") #ระยะทางเกิน25กิโลเมตร #แรกเข้า+คิดเพิ่มเกิน25 กม.
else :
    print("Error")


#โปรแกรมหาผลรวม
i=1
sum=0
loop = int(input("กรุณากรอกจำนวนครั้งในการรับค่า  : "))
while( i <= loop ) : 
    a = int(input("กรอกตัวเลข : "))
    sum+=a
    i+=1
print("ผลรวมทั้งหมด = ", sum)

print("ป้อนชื่ออาหารสุดโปรด หรือ exit เพื่ออกจากโปรแกรม")
foodlist = []
i=1
y=0
while(i<100):
    food = str(input("อาหารโปรดอันดับที่ "+str(i)+" : "))
    if (food == 'exit') :
        break
    foodlist.append(food)
    i+=1
print("อาหารสุดโปรดของคุณคือ")
for x in foodlist :
    y+=1
    print(str(y)+"."+str(x), end ='      ')


    '''number1 = input("Input First number : ") #การเปรียบเทียบ Boollen
number2 = input("Input Second number : ")
print(number1, "=" ,number2, ":" ,number1 == number2)
print(number1, ">" ,number2, ":" ,number1 > number2)
print(number1, "<" ,number2, ":" ,number1 < number2)

print(bool("Hello"))
print(bool(""))

x = ["comED" , "KKU"]
y = ["comED" , "KKU"]
print("com"in x) 

a = 60
b = 13
c = 0

c = a & b           #12 = 0000 1100
print(c)

c = a | b           #61 = 0011 1101
print(c)

c = a ^ b           #49 = 0011 0001
print(c)

c = ~a              #-61 = 1100 0011
print(c)

c = a << 2          #
print(c)

c = a >> 2
print(c) 

print("Day Converter Program")
day = input("Input Number of Day --> ")
print(day, "Day --> Hours" ,int(day)*24, "Hours" )
print(day, "Day --> Minutes" ,int(day)*1440, "Minutes" )
print(day, "Day --> Seconds" ,int(day)*86400, "Seconds" )

thislist = [ "com", "ED" , "KKU" , 99]
thislist[0] = "ComED"
print(thislist)

friend = ["jan", "cream" , "phu" , "bam" , "aom" , "pee" , "bas" , "kong" , "da" , "james"]
friend[9] = "may" 
friend[3] = "boat"
print(friend[-10])

friend = ["jan", "cream" , "phu" , "bam" , "aom" , "pee" , "bas" , "kong" , "da" , "james"]
#friend[9] = "may" 
#friend[3] = "boat"
friend.append("dome")
friend.append("poondang")
friend.insert(1,"c-za")
friend.insert(8,"ped")
friend.remove("aom")
friend.pop()
friend.pop(3)
del friend[7]
friend.clear()
del friend
print(friend)

animal = {"cat","dog","rat","pig","ant"}
animal.add("monkey")
animal.update(["python","capibara","spider","wombet","penguin","crocodile"])
print(animal)

#โปรแกรมหยิบสินค้าใส่ตระกร้า
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("โปรดหยิบสินค้าใส่ตระกร้า")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

a = input("หยิบสินค้าครั้งที่ 1 :")
b = input("หยิบสินค้าครั้งที่ 2 :")
c = input("หยิบสินค้าครั้งที่ 3 :")
d = input("หยิบสินค้าครั้งที่ 4 :")
e = input("หยิบสินค้าครั้งที่ 5 :")
basket = []
basket.append(a)
basket.append(b)
basket.append(c)
basket.append(d)
basket.append(e)
print('1.',basket[0])
print('2.',basket[1])
print('3.',basket[2])
print('4.',basket[3])
print('5.',basket[4])'''

print("โปรแกรมคำนวนค่าผ่านทางมอเตอร์เวย์")
print("-------------------------------")
print("รถยนต์ 4 ล้อ           กด 1")
print("รถยนต์ 6 ล้อ           กด 2")
print("รถยนต์มากกว่า 6 ล้อ     กด 3\n")

thisdict1 = {
    "ลาดกระบัง-บางบ่อ" : "25 บาท",
    "ลาดกระบัง-บางประกง" : "30 บาท",
    "ลาดกระบัง-พนัสนิคม" : "45 บาท",
    "ลาดกระบัง-บ้านบึง" : "55 บาท",
    "ลาดกระบัง-บางพระ" : "60 บาท",
}
thisdict2 = {
    "ลาดกระบัง-บางบ่อ" : "45 บาท",
    "ลาดกระบัง-บางประกง" : "45 บาท",
    "ลาดกระบัง-พนัสนิคม" : "75 บาท",
    "ลาดกระบัง-บ้านบึง" : "90 บาท",
    "ลาดกระบัง-บางพระ" : "100 บาท",
}
thisdict3 = {
    "ลาดกระบัง-บางบ่อ" : "60 บาท",
    "ลาดกระบัง-บางประกง" : "70 บาท",
    "ลาดกระบัง-พนัสนิคม" : "110 บาท",
    "ลาดกระบัง-บ้านบึง" : "130 บาท",
    "ลาดกระบัง-บางพระ" : "140 บาท",
}

car = int(input("เลือกประเภทยานพาหนะ "))

if car==1:
    print("ค่าบริการรถยนต์ 4 ล้อ\n")
    print(*thisdict1.items(), sep = "\n")
if car==2:
    print("ค่าบริการรถยนต์ 6 ล้อ\n")
    print(*thisdict2.items(), sep = "\n")
if car==3:
    print("ค่าบริการรถยนต์มากกว่า 6 ล้อ\n")
    print(*thisdict3.items(), sep = "\n")

"""

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