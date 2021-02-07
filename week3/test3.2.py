#โปรแกรมหาผลรวม
i=1
sum=0
loop = int(input("กรุณากรอกจำนวนครั้งในการรับค่า  : "))
while( i <= loop ) : 
    a = int(input("กรอกตัวเลข : "))
    sum+=a
    i+=1
print("ผลรวมทั้งหมด = ", sum)