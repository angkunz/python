choice = 0
word = []
kind = []
mean = []

def menu() :
    global choice
    print('Menu\n 1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์\n 3.ลบคำศัพท์\n 4.Exit')
    choice = input('Select Menu :')

def update() :
    Input_word = input('เพิ่มคำศัพท์ : ')
    word.append(Input_word)
    Input_kind = input('ชนิดของคำศัพท์ n. , v. , adj. , adv : ')
    kind.append(Input_kind)
    Input_mean = input('ความหมาย : ')
    mean.append(Input_mean)
    print('เพิ่มคำศัพท์เรียบร้อยแล้ว')

def show() :
    x=0
    i = ''
    i=len(word)
    print('-'*30)
    print('คำศัพท์ทั้งหมด'+ str(i)+ 'คำ')
    print('-'*30)
    print('')
    while True :
        print(word[x]+'  ' +kind[x]+'  ' +mean[x])
        x+1

while True :
    menu()
    if choice == '1' :
        update()
    elif choice == '2' :
        show()
    else:
        break



'''def Introduce(arg1, arg2 = 'com',arg3 = 'ed',arg4 = 'kku') :
    print('Hello I am '+arg1+','+arg2+','+arg3+','+arg4)

Introduce('Pythton')
Introduce(arg1= 'Python')
Introduce(arg1 = 'Python',arg3 = 'Sci')
Introduce('Python',arg4 = 'CMU')

import os
choice = 0
filename = ''

def menu() :
    global choice
    print('Menu\n 1.Open Calculator\n 2.Open Notepad\n 3.Exit')
    choice = input('Select Menu :')

def opennotepad():
    filename = 'C:\Windows\notepad.exe'
    print('Memorandum writing %s ' %filename)
    os.system(filename)

def opencalculator():
    filename = 'C:\Windows\SysWOW64\calc.exe'
    print("Calculate Number %s" %filename)
    os.system(filename)

while True :
    menu()
    if choice == '1' :
        opencalculator()
    elif choice == '2' :
        opennotepad()
    else:
        break
    '''

'''choice = 0
select = []

def menu() :
    global choice
    print('Menu\n 1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตระกร้า\n 3.แสดงรายการสินค้าที่หยิบ\n 4.Exit')
    choice = input('Select Menu :')

def shop_list() :
    print('รายการสินค้า\n 1.โค้กกระป๋อง\n 2.M150\n 3.โออิชิกรีนที\n 4.น้ำเปล่า\n 5.มาม่า')

def Select_shop() :
    print('กรุณาเลือกรายการสินค้า\n 1.โค้กกระป๋อง ราคา 10 บาท\n 2.M150 ราคา 10 บาท\n 3.โออิชิกรีนที ราคา 20 บาท\n 4.น้ำเปล่า ราคา 7 บาท\n 5.มาม่า ราคา 6 บาท')

    while True :
        a = int(input('เลือกหยิบสินค้าหมายเลข : '))
        if a == 1 :
            b = 'โค้กกระป๋อง ราคา 10 บาท'
            select.append(b)
        elif a == 2 :
            b = 'M150 ราคา 10 บาท'
            select.append(b)
        elif a == 3 :
            b = 'โออิชิกรีนที ราคา 20 บาท'
            select.append(b)
        elif a == 4 :
            b = 'น้ำเปล่า ราคา 7 บาท'
            select.append(b)
        elif a == 5 :
            b = 'มาม่า ราคา 6 บาท'
            select.append(b)
        else :
            break

Select_shop()
print(select)
'''