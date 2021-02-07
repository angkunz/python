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