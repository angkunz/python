print("*"*30)
print('โปรแกรมรับคะแนนนักเรียน')
print("*"*30)
student = int(input("กรุณากรอกจำนวนนักเรียน : "))
point_list = [0,0,0,0,0,0]
score = ['90 - 100' +':','80 - 89' +'\t:','70 - 79' +'\t:','60 - 69' +'\t:','50 - 59' +'\t:',' 0 - 49' +'\t:']
x = 1
while x <= student :
    point = int(input("กรุณากรอกคะแนน นักเรียนคนที่ "+str(x)+" : "))
    if point <= 100 and point >= 90 : 
        point_list[0]+=1
    elif point <= 89 and point >= 80 :
        point_list[1]+=1
    elif point <= 79 and point >= 70 :
        point_list[2]+=1
    elif point <= 69 and point >= 60 :
        point_list[3]+=1
    elif point <= 59 and point >= 50 :
        point_list[4]+=1
    elif point <= 49 and point >= 0 :
        point_list[5]+=1
    else :
        print('กรอกคะแนนผิดพลาด กรุณาลองอีกครั้ง')
        continue
    x+=1
for x in range(0,6) :
    print(score[x],'*'*point_list[x])

